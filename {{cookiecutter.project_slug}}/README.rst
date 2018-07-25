============================================================
{{ cookiecutter.project_slug }}: {{ cookiecutter.project_name }}
============================================================

.. start-badges

.. image:: ../logo.jpg
    :target: http://gramaziokohler.arch.ethz.ch/
    :alt: GKR

.. end-badges

.. start-project description

**{{ cookiecutter.project_short_description }}** ...


Main features
-------------

* feature
* feature
* more features

**{{ cookiecutter.project_slug }}** runs on Python x.x and x.x.


Documentation
-------------

.. Explain how to access documentation: API, examples, etc.

..
.. optional sections:

Requirements
------------

.. Write requirements instructions here


Installation
------------

.. Write installation instructions here


Contributing
------------

Make sure you setup your local development environment correctly:

* Clone the `{{cookiecutter.project_slug}} <https://github.com/gramaziokohler/{{cookiecutter.project_slug}}>`_ repository.
* Install development dependencies and make the project accessible from Rhino:

::

    pip install -r requirements-dev.txt
    invoke add-to-rhino

**You're ready to start working!**

During development, use tasks on the
command line to ease recurring operations:

* ``invoke clean``: Clean all generated artifacts.
* ``invoke check``: Run various code and documentation style checks.
* ``invoke docs``: Generate documentation.
* ``invoke test``: Run all tests and checks in one swift command.
* ``invoke add-to-rhino``: Make the project accessible from Rhino.
* ``invoke``: Show available tasks.

For more details, check the `Contributor's Guide <CONTRIBUTING.rst>`_.


Releasing this project
----------------------

.. Write releasing instructions here


.. end of optional sections
..

Credits
-------------

This package was created by {{ cookiecutter.full_name }} <{{ cookiecutter.email }}> `@{{ cookiecutter.github_username }} <https://github.com/{{ cookiecutter.github_username }}>`_ at Gramazio Kohler Research `@gramaziokohler <https://github.com/gramaziokohler>`_
