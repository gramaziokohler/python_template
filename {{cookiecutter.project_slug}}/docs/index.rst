============================
{{cookiecutter.project_slug}}: {{cookiecutter.project_name}}
============================

.. start-badges

{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%} {% for _ in cookiecutter.project_name %}={% endfor %} {{ cookiecutter.project_name }} {% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %} .. image:: https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}.svg

.. image:: file
    :target: link
    :alt: title

.. end-badges

.. start-project description

**{{cookiecutter.project_name}}** ...


========
Contents
========

.. toctree::
   :maxdepth: 2

   readme
   reference/index
   contributing
   authors
   changelog

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
