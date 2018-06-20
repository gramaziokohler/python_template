#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import codecs
import os
import subprocess
import sys
from xml.dom.minidom import parse

try:
    input = raw_input
except NameError:
    pass


print('Initializing Git repository...')
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '--quiet', '-m', 'Initial commit'])
subprocess.call(['git', 'remote', 'add', 'origin',
                 'https://github.com/gramaziokohler/{{cookiecutter.project_slug}}.git'])

print('Installing development workflow dependencies...')
subprocess.call(['pip', 'install', '-q', '-r', 'requirements-dev.txt'])

{% if cookiecutter.add_to_rhino_python == "yes" %}

# The following code is based on gh_python_remote
# https://github.com/Digital-Structures/ghpythonremote
# MIT License
# Copyright (c) 2017 Pierre Cuvilliers, Caitlin Mueller, Massachusetts Institute of Technology


def get_ironpython_path(rhino_version):
    appdata_path = os.getenv('APPDATA', '')
    ironpython_settings_path = os.path.join(appdata_path, 'McNeel', 'Rhinoceros', rhino_version, 'Plug-ins',
                                            'IronPython (814d908a-e25c-493d-97e9-ee3861957f49)', 'settings')

    if not os.path.isdir(ironpython_settings_path):
        print('IronPython directory for Rhinoceros not found in {!s}.\n'.format(
            ironpython_settings_path))
        print('Cannot automatically make this project available to IronPython')
        print(
            'To add manually, open EditPythonScript on Rhinoceros, go to Tools -> Options')
        print('and add the project path to the module search paths/')
        raise RuntimeError('No IronPython folder found in %APPDATA%')

    return ironpython_settings_path


def replaceText(node, newText):
    if node.firstChild.nodeType != node.TEXT_NODE:
        raise Exception("Node does not contain text")

    node.firstChild.replaceWholeText(newText)


def updateSearchPaths(settings_file, python_source_path):
    with codecs.open(settings_file, 'r', encoding="ascii", errors="ignore") as file_handle:
        doc = parse(file_handle)

    for entry in doc.getElementsByTagName('entry'):
        if entry.getAttribute('key') == 'SearchPaths':
            current_paths = entry.firstChild.data
            if python_source_path not in current_paths:
                replaceText(entry, current_paths + ';' + python_source_path)

    with codecs.open(settings_file, 'w', encoding='utf-8') as file_handle:
        doc.writexml(file_handle)


try:
    python_source_path = os.path.join(os.getcwd(), 'src')
    rhino_setting_per_version = [
        ('5.0', 'settings.xml'), ('6.0', 'settings-Scheme__Default.xml')]
    for version, filename in rhino_setting_per_version:
        settings_file = os.path.join(get_ironpython_path(version), filename)
        if not os.path.isfile(settings_file):
            print('Cannot find IronPython settings file for Rhino ' + version)
        else:
            updateSearchPaths(settings_file, python_source_path)
            print('Updated search path for Rhino ' + version)

except RuntimeError as error:
    print(error)

{% endif %}


def confirm(question):
    while True:
        response = input(question).lower().strip()

        if not response or response in ('n', 'no'):
            return False

        if response in ('y', 'yes'):
            return True

        print('Focus, kid! It is either (y)es or (n)o', file=sys.stderr)


print('\n\nSetup completed SUCCESSFULLY!\n')

print('AND NOW WHAT?')
print('-------------\n')

print('You can go to the project folder:\n')
print('  cd {{cookiecutter.project_slug}}\n')
print('And see which tasks are available:\n')
print('  invoke help\n\n')
{% if cookiecutter.add_to_rhino_python == "yes" %}
print('You can also open Grasshopper, add a Python script component and type the following:\n\n')
print('import {{cookiecutter.project_slug}}')
print('print ({{cookiecutter.project_slug}}.__file__)\n\n')
{% endif %}

print('GITHUB')
print('------\n')

print('To push your code to GitHub:\n')

print('Go to this link and create an EMPTY repository named \'{{cookiecutter.project_slug}}\',\n')
print('Add a description, make it Private, and DO NOT select "Initialize with a README":\n')
print('  https://github.com/organizations/gramaziokohler/repositories/new\n')

if confirm('ARE YOU DONE? If so, we can link github automatically for you?\n(y)es, link now | (n)o, I will do it myself later: '):
    subprocess.call(['git', 'push', '--quiet', '-u', 'origin', 'master'])
else:
    print('\nNo worries, you can finalize the link to github later running the following:\n')
    print('  git push -u origin master\n')
