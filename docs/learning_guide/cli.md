# How to create a CLI with [**Typer**](https://github.com/tiangolo/typer)?

!!! abstract "Learning Objectives"
    By the end of this section, you should be able to:

    * Explain why **Typer** is an optimal choice to build your CLI
    * Navigate the official documentation of **Typer** 
    * Build your own CLI from scratch 
    * Automatically generate documentation for your CLI
    * Explain how `quizli's` CLI was built
    
## What is **Typer** and why should I use it?

!!! quote
    **Typer** is a library for building CLI applications that users will love using and developers will love creating. Based on Python 3.6+ type hints.

Maybe you have heard of or even used [**Click**](https://click.palletsprojects.com/en/8.0.x/) before - a popular Python package for creating command line interfaces in Python.
Since **Typer** is based on Click, by using it you get all of Clicks's features, plus everything Typer adds on top of it.

For me the most striking features/advantages of Typer are that it: 

- Utilizes [Python's type hints](https://www.python.org/dev/peps/pep-0484/)
- Provides automatic help, and automatic completion (for most/all shells)
- Allow to [generate Markdown documentation](https://typer.tiangolo.com/typer-cli/#generate-docs-with-typer-cli) for your CLI's build with Typer (see below)
- Has sensible defaults (allows to write less code)
- Is easy to use both for developers _and_ users
- Contains a comprehensive documentation with lot's of examples and detailed tutorials

There is also a [particular section in Typer's docs](https://typer.tiangolo.com/alternatives/) on how it compares to alternative libraries.

!!! info "Recommended Reading"
    - [Typer's Intro](https://typer.tiangolo.com/)
    - [Typer's User Tutorial](https://typer.tiangolo.com/tutorial/)

## Using **Typer** for `quizli`

### Creating a CLI for `quizli`

Below you see the source code of `quizli's` CLI. We added comments, prepended with (1) to (4) and highlighted in yellow, to explain 
how the source code relates to the resulting CLI app.


``` py title="quizli's CLI"

--8<-- "quizli/main.py"
```


### Generating Markdown documentation


Take a look at the [CLI reference page](../user_guide/cli.md) in `quizli's` user guide section.

What you see there was actually automatically generated with **Typer**, using a single, simple command:

```
typer quizli/main.py utils docs --name quizli --output docs/user_guide/cli.md
```

This feature allows you to write all the documentation of your CLI directly within the source file(s) simply using Python docstrings. 
This way, following the [DRY principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)[^1], it is easy to keep your docs up-to-date and
in-sync with the source code.

[^1]: The DRY principle is stated as "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system"

## Final remarks

With our example we only scratch the surface of what is possible with **Typer**, and what is needed for a CLI 
to be useful in a real-world scenario. But it should get you going! :)

!!! hint "A note about Best Practices"
    As soon as you are building a larger "real-world" CLI, it pays of for you and your users to adhere to some _best practices_:

    A comprehensive and elucidating guideline can be found here: [https://clig.dev/](https://clig.dev/).
