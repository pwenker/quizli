"""
This module contains examples showing how to dynamically create a 'builtin'-quiz.

- `python_quiz`
- `binary_number_quiz`
"""

import importlib
from pkgutil import iter_modules

from rich import print
from rich.prompt import IntPrompt, Prompt
from rich.rule import Rule

from quizli import Quiz, QuizItem, StrEnum
from quizli.utils import em

__all__ = [
    "PyQuizCategory",
    "PythonModule",
    "QuizKind",
    "binary_number_quiz",
    "python_quiz",
]


class QuizKind(StrEnum):
    """
    This enumeration holds all quiz variants.

    By adding the name of your quiz function as a variant,
    it will automatically show up as an option in quizli's
    CLI.
    """

    PYTHON_QUIZ = "python_quiz"
    BINARY_NUMBER_QUIZ = "binary_number_quiz"


class PyQuizCategory(StrEnum):
    """
    The category of the Python Quiz
    """

    MODULES = "modules"
    OBJECTS = "objects"


installed_modules = [mod.name for mod in iter_modules() if mod.ispkg]
PythonModule = StrEnum("PythonModule", {mod.upper(): mod for mod in installed_modules})


def python_quiz() -> Quiz:

    """Make a quiz about Python

    This function let's the user interactively create one of the following
    two quiz types:

    1. A quiz that shows the description of Python modules in the question field
    and asks the user for the name of the respective modules
    2. A quiz that shows the description of Python objects of a chosen module
    in the question field and asks the user for the name of respective function/method/class.

    Returns:
        Quiz: The interactively created Python quiz

    """
    print(Rule(f':snake: Welcome to the built-in {em("Python quiz")} :snake:'))

    category = Prompt.ask(
        f"Do you want to be quizzed on {em('modules')} or {em('objects')}?",
        choices=[c for c in PyQuizCategory],
        default=PyQuizCategory.OBJECTS,
    )

    if category == PyQuizCategory.MODULES:
        quiz_items = [
            QuizItem(
                question=importlib.import_module(module).__doc__,
                answer=importlib.import_module(module).__name__,
            )
            for module in PythonModule
        ]
        return Quiz(
            name="What's the name of the module?",
            items=quiz_items,
        )
    else:
        module_name = Prompt.ask(
            ":boom: Choose one of your installed modules :boom:",
            choices=[m for m in PythonModule],
            default="quizli",
        )
        module = importlib.import_module(module_name)

        quiz_items = [
            QuizItem(
                question=object.__doc__,
                answer=object.__name__,
            )
            for _, object in module.__dict__.items()
            if hasattr(object, "__name__")
        ]
        return Quiz(
            name="What's the name of the object?",
            items=quiz_items,
        )


def binary_number_quiz() -> Quiz:
    """Make a quiz about binary numbers

    This function creates a quiz about conversion of
    binary numbers into their decimal representation.

    Returns:
        Quiz: The interactively created binary number quiz

    """
    print(
        Rule(
            f':keycap_2: Welcome to the built-in {em("Binary number quiz")} :keycap_2:'
        )
    )

    largest_number = IntPrompt.ask(
        "What should be the largest number in the binary quiz?",
        default=1000,
    )
    quiz_items = [
        QuizItem(question=f"{x:b}", answer=str(x)) for x in range(largest_number)
    ]
    return Quiz(
        name="What's the decimal expression of this binary number?",
        items=quiz_items,
    )
