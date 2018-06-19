# python_template

A template for GKR python projects

## Features

* Project folder and file skeleton
* Documentation based on [Sphinx](http://www.sphinx-doc.org/en/master/)/[reStructuredText](http://docutils.sourceforge.net/rst.html)
* Testing framework: [pytest](https://docs.pytest.org/en/latest/)
* Basic setup script to create pip installable packages
* Automation of common tasks for development workflow based on [pyinvoke](http://www.pyinvoke.org/) (generate documentation, run tests, check format, etc.)

## Requirements

Install `cookiecutter` command line: `pip install cookiecutter`

## Usage

Generate a new Cookiecutter template layout:
```
$ cookiecutter https://github_username:github_password@github.com/gramaziokohler/python_template.git
```

Go to project folder:

```
$ cd <project-slug>
```

Now you can see which tasks are available:

```
$ invoke help
```

## License

This template is licensed under the terms of the [MIT License](/LICENSE)
