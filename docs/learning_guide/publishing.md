# Managing and Publishing with [**Poetry**](https://python-poetry.org/)

!!! abstract "Learning Objectives"
    By the end of this section, you should be able to:

    * Explain _what_ Poetry is.
    * Explain _why_ Poetry is a great choice for dependency management and packaging in Python.
    * Explain what a `pyproject.toml` file is and how it is useful.
    * Publish your own package with Poetry
    
## What is **Poetry**?

???+ question "What is Poetry?"
    
    !!! quote 
        Poetry is a tool for **dependency management** and **packaging** in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

!!! example "Basic poetry usage/workflow"
    Read poetry's [basic usage guide](https://python-poetry.org/docs/master/basic-usage/)


## What's that `pyproject.toml` file?

We answer the following questions by referring to the relevant sections in **PEP 518**. 
This saves us some time, avoids reproducing existing information, and you end up with some experience reading through PEP's :).

!!! question "What was the rationale behind PEP518 and the `pyproject.toml` file? :material-arrow-right: [Answer](https://www.python.org/dev/peps/pep-0518/#rationale)"
!!! question "Why was the TOML format chosen? :material-arrow-right: [Answer](https://www.python.org/dev/peps/pep-0518/#file-format)"
!!! question "Why where YAML, JSON, and the configparser rejected? :material-arrow-right: [Answer](https://www.python.org/dev/peps/pep-0518/#json)"

To see the `pyproject.toml` file in action, take a look at the following example.

### Example: `quizli's` `pyproject.toml` file
!!! example
    ``` py title="pyproject.toml"

    --8<-- "pyproject.toml"
    ```

!!! tip "Poetry's new dependency groups"
    With version 1.2.0 poetry allows you to organize your dependencies by groups. 
    
    For more information about this **dependency groups** feature, see
    the [Managing dependencies section](https://python-poetry.org/docs/master/managing-dependencies/)
    in the docs.

## Publishing the package

``` py title="Github Workflow to Publish Package"

--8<-- ".github/workflows/publish_package.yml"
```

!!! info "Resources"
    - [PEP 517 - A build-system independent format for source trees](https://www.python.org/dev/peps/pep-0517/)
    - [PEP 518 - Specifying Minimum Build System Requirements for Python Projects](https://www.python.org/dev/peps/pep-0518/)


