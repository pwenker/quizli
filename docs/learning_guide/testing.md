# How to test your app?

!!! abstract "Learning Objectives"
    By the end of this section (if you work on the assignments), you should know how to:

    * Create basic tests for your CLI with `pytest` and `typer`
    * Test your APIs with `doctest` (via `pytest`)
    * Add a CI/CD pipeline for automatic testing
    
You made it to the last section of the learning guide! Kudos! :partying_face:

Testing software is a wonderful but complicated endeavor. A thorough discussion of all the facets of testing is beyond the scope of this section.

But we do want to emphasize the crucial role that testing plays in software development. 
So we at least provide you with some basic examples and then point to resources for further learning.

Since this is the last chapter of the learning guide, we are going to challenge you a bit more:
we leave out extensive explanations and instead let you work through assignments. We hope this will help you deepening your understanding and prepare you for your next
steps on your journey to become a great Pythonista and open-source contributor! :material-language-python:

## Testing your CLI with `pytest` and `Typer`

!!! assignment "Assignment 1"
    - a) Read through: [https://typer.tiangolo.com/tutorial/testing/](https://typer.tiangolo.com/tutorial/testing/)
    - b) Read through: [https://docs.pytest.org/en/7.0.x/getting-started.html](https://docs.pytest.org/en/7.0.x/getting-started.html)
    - c) Add useful tests to `tests/test_quizli.py` (shown below) to improve the code coverage.
    
``` py title="test_quizli.py"

--8<-- "tests/test_quizli.py"
```

## Testing your docstring examples with `doctest`

!!! assignment "Assignment 2"
    - Read through: [`doctests` - Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
    - Read through: [`pytest` - Doctest integration for modules and test files](https://docs.pytest.org/en/6.2.x/doctest.html)

???+ question "What is `doctest` good for?"
    !!! quote
        The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. 
        There are several common ways to use doctest:

        - To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.
        - To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
        - To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.

!!! example 
    ```
    @dataclass
    class QuizItem:
        """Represents a quiz item - a question-answer pair

        Attributes:
            question: The question of the quiz item
            answer: The answer of the quiz item

    {==
        Examples:
            >>> quiz_item = QuizItem(question='What is the meaning of life?', answer=42)

            >>> quiz_item
            QuizItem(question='What is the meaning of life?', answer=42)

            >>> quiz_item.question
            'What is the meaning of life?'

            >>> quiz_item.answer
            42
        """
    ==}

    (...)
    ```
    
!!! hint
    We can run`pytest` with the `--doctest-modules` flag to test whether all docstring examples are correct and up-to-date.

## Automate testing with a CI/CD pipeline

!!! assignment "Assignment 3"
    - a) Read through Github's [CI/CD: The what, why, and how](https://resources.github.com/ci-cd/)
    - b) Read through: [https://github.com/snok/install-poetry](https://github.com/snok/install-poetry)
    - c) Read through `.github/workflows/test_package.yml` (shown below) and then explain it to someone.
    
``` yaml title="CI/CD workflow"

--8<-- ".github/workflows/test_package.yml"
```


## Real-world testing

We already told you that testing is hard. And there is a lot to learn to do it right. 
Before we part, here is a list with key concepts you can explore to ease your way into the world of testing.

!!! assignment "Assignment 4: Key Concepts in the testing world"
    - a) What is **test-driven development**?
    - b) What is **property-based testing**?
    - c) How can you utilize **tests as documentation**?
    - d) What is **unit testing**? And what is **integration testing**?
    - e) What is **code coverage**?

