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
* Minimal [Travis-CI integration](https://travis-ci.org)

## What's included

* Folder structure:
  * `docs` directory with a pre-configured Sphinx documentation setup
  * `src` directory where to place all the files containing code. It includes a `__init__.py` to make Python treat the project directories as containing packages. It also includes a documentation example for a sample class and sample function.
  * `tests` directory containing a basic unit test using pytest
* Files at root:
  * `README.rst` used as a GitHub project summary page
  * `setup.py` used to generate project install and releases
  * `tasks.py` used to automate common tasks
  * `.travis.yml` file with a minimal configuration to integrate with Travis CI. 
  * `.editorconfig` file for defining coding styles
  * `CONTRIBUTING.rst` guide to use when sending a pull request or an issue on GitHub
  * `CHANGELOG.rst` which contains a chronologically ordered list of notable changes for each version of a project
  * `.github/ISSUE_TEMPLATE` folder to guide others to report issues and feature request to GitHub
  * `requirements-dev.txt` file with a list of installed dependencies
  * `LICENSE` file that defaults to MIT License

## Requirements

Install `Git SCM` from https://git-scm.com/

Install `cookiecutter` command line: `pip install cookiecutter`

## Usage

In the terminal, go to the folder where you want to place your project:
```
$ cd <your-projects-folder>
```

Generate a new Cookiecutter template layout:
```
$ cookiecutter gh:gramaziokohler/python_template
```

Go to project folder:

```
$ cd <project-slug>
```

Now you are ready to install the newly created project. It is recommended that you create a `conda` environment for it, for instance, if you plan to use Python 3.8 you could create it with the following command:

```
$ conda create -n NAME_OF_YOUR_PROJECT_ENV python=3.8
```

Activate the environment:

```
$ conda activate NAME_OF_YOUR_PROJECT_ENV
```

Now we are ready to install the project that we have just created:

```
$ pip install -r requirements-dev.txt
```

To see which automation tasks are available, use:

```
$ invoke help
```

## Additional settings

To use the coding style feature with [EditorConfig](https://editorconfig.org/):

* Some text editors have a native EditorConfig. If yours doesn't you can download the appropriate plugin [here](https://editorconfig.org/#download).

To activate Continuous Integration:

* [Enable the repository in your Travis CI account](https://travis-ci.org/profile).

## License

This template is licensed under the terms of the [MIT License](/LICENSE)
