"""
This module contains the main building blocks of the quiz logic.

* The `QuizItem` class represents a question-answer pair
* The `Quiz` class contains a list of `QuizItem's` containing the quiz data
* The `QuizConfig` class serves to configure quiz settings 
* The `QuizMode` enumeration serves to set the quiz mode

"""

import csv
import random
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Dict, List

from rich.prompt import Prompt

__all__ = ["StrEnum", "QuizMode", "QuizConfig", "QuizItem", "Quiz"]


class StrEnum(str, Enum):
    """
    We define this `StrEnum` class for convenience.
    Later on we will define a few Enums that will inherit from it,
    and we will then use them in our CLI as parameter choices:

    Resources:
        * https://docs.python.org/3/library/enum.html
        * https://typer.tiangolo.com/tutorial/parameter-types/enum/
    """


class QuizMode(StrEnum):
    """Select the mode of the quiz

    Attributes:
        SUDDEN_DEATH: Finish the quiz if user answers incorrectly
        COMPLETE: Go through the whole quiz in any case
    """

    SUDDEN_DEATH = "sudden_death"
    COMPLETE = "complete"


@dataclass
class QuizConfig:
    """Allows configuring the quiz settings

    Attributes:
        mode: Sets the mode of the quiz (See `QuizMode`)
        randomize: Whether the quiz should be shuffled

    """

    mode: QuizMode = QuizMode.SUDDEN_DEATH
    randomize: bool = True


@dataclass
class QuizItem:
    """Represents a quiz item - a question-answer pair

    Attributes:
        question: The question of the quiz item
        answer: The answer of the quiz item

    Examples:
        >>> quiz_item = QuizItem(question='What is the meaning of life?', answer=42)

        >>> quiz_item
        QuizItem(question='What is the meaning of life?', answer=42)

        >>> quiz_item.question
        'What is the meaning of life?'

        >>> quiz_item.answer
        42
    """

    question: str
    answer: str

    def ask(self, show_question: bool = True) -> bool:
        """Show a question and prompt for an answer

        This method shows the user a question and
        returns whether the user typed the correct.
        answer.

        Args:
            show_question: Whether to show the question
        Returns:
            bool: Whether the question as answered correctly
        """
        if show_question:
            print(f"Question: {self.question}")
        guess = Prompt.ask("Answer")
        return guess == self.answer


@dataclass
class Quiz:
    """
    The `Quiz` dataclass contains the quiz data along with some functionality.

    Attributes:
        items: The items of the quiz (question-answer pairs)
        name: The name of the quiz

    Examples:
        Create a quiz from a csv file
        >>> quiz = Quiz.from_csv(file_name='examples/quiz.csv', name='Example Quiz')


    """

    items: List[QuizItem]
    name: str = "Quiz"

    def __len__(self):
        return len(self.items)

    @classmethod
    def from_dict(cls, questions_and_answers: Dict, name: str) -> "Quiz":
        """Create a Quiz instance from a dictionary

        This classmethod accepts a dictionary and a name
        and then instantiates and returns a quiz from it.

        Args:
            questions_and_answers: The dictionary containing questions and answers
            name: The name of the quiz

        Returns:
            Quiz: The quiz instance generated from the dictionary
        """
        return cls(
            items=[QuizItem(q, a) for q, a in questions_and_answers.items()], name=name
        )

    @classmethod
    def from_csv(cls, file_name: Path, name: str = "") -> "Quiz":
        """Create a Quiz instance from a csv file

        This classmethod accepts a file path and an optional
        name and then instantiates and returns a quiz from it.

        Args:
            file_name: The path of the csv file
            name: An optional name for the quiz. If not given,
                it will fallback to the file name.

        Returns:
            "Quiz": The quiz instance generated from the csv file
        """
        quiz_name = name if name else file_name.stem
        with open(file_name, newline="") as f:
            quiz = cls(items=[QuizItem(q, a) for q, a in csv.reader(f)], name=quiz_name)
        return quiz

    def show(self) -> None:
        """Show the items of the quiz"""
        for item in self.items:
            print(item)

    def shuffle(self) -> None:
        """Shuffle the items of the quiz"""
        random.shuffle(self.items)
