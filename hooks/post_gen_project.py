#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import subprocess

print('Initializing Git repository...')
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '--quiet', '-m', 'Initial commit'])
subprocess.call(['git', 'remote', 'add', 'origin',
                 'https://github.com/gramaziokohler/{{cookiecutter.project_slug}}.git'])

print('Installing development workflow dependencies...')
subprocess.call(['pip', 'install', '-q', '-r', 'requirements-dev.txt'])

print('\nSetup completed SUCCESSFULLY!\n\n')

print('To push your code to GitHub:\n')

print('Go to this link and create an EMPTY repository named \'{{cookiecutter.project_slug}}\',\n')
print('Add a description, make it Private, and DO NOT select "Initialize with a README":\n')
print(' https://github.com/organizations/gramaziokohler/repositories/new')

print('After that, you can go to the project folder:\n')
print('  cd {{cookiecutter.project_slug}}\n')
print('And see which tasks are available:\n')
print('  invoke help\n')
