# python_template

This project automates the set up of a new python-based project using a Cookiecutter template.

[Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/readme.html#) is a command-line utility that lets you quickly bootstrap a new project from a template. It takes a directory tree and copies it into your new project, replacing all the generic info that finds surrounded by templating tags `{{` and `}}` with your project info written in `cookiecutter.json`.

## Features

* Project directory and file structure
* Documentation based on [Sphinx](http://www.sphinx-doc.org/en/master/)/[reStructuredText](http://docutils.sourceforge.net/rst.html)
* Testing framework: [pytest](https://docs.pytest.org/en/latest/)
* Basic setup script to create pip installable packages
* Automation of common tasks for development workflow based on [pyinvoke](http://www.pyinvoke.org/) (generate documentation, run tests, check format, etc.)
* [EditorConfig](https://editorconfig.org/) integration

## What's included

* A `docs` directory with a pre-configured Sphinx documentation setup
* A `src` directory where to place all the files containing code. It includes a `__init__.py` to make Python treat the project directories as containing packages. It also includes a documentation example for a sample class and sample function.
* A `tests` directory containing a basic unit test using pytest

* A `README.rst` used as a GitHub project summary page
* A `setup.py` used to generate project install and releases
* A `tasks.py` used to automate common tasks
* A `.editorconfig` file for defining coding styles
* A `CONTRIBUTING.rst` guide to use when sending a pull request or an issue on GitHub
* A `CHANGELOG.rst` which contains a chronologically ordered list of notable changes for each version of a project
* A `ISSUE_TEMPLATE.md` guide for when posting issues on GitHub
* A `requirements-dev.txt` file with a list of installed dependencies
* A `LICENSE` file that defaults to MIT License

## Requirements

Install `cookiecutter` command line: `pip install cookiecutter`

## Usage

In the terminal, go to the folder where you want to place your project:
```
$ cd ..
```

Generate a new Cookiecutter template layout:
```
$ cookiecutter gh:gramaziokohler/python_template
```

Go to project folder:

```
$ cd <project-slug>
```

Now you can see which tasks are available:

```
$ invoke help
```

## Additional settings

To use the coding style feature with [EditorConfig](https://editorconfig.org/):

* Some text editors have a native EditorConfig. If yours doesn't you can download the appropriate plugin [here](https://editorconfig.org/#download).

## License

This template is licensed under the terms of the [MIT License](/LICENSE)
