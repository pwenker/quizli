"""
This module contains all the layout logic.

- We define a `QuizLayoutBase` abstract base class.
- We define a `QuizLayout` base class.

"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Union

from rich import print
from rich.align import Align
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn

from quizli import QuizItem
from quizli.utils import em, motivate

__all__ = ["QuizLayoutBase", "FancyQuizLayout"]


class QuizLayoutBase(ABC):
    """This abstract base class serves as blueprint for `QuizLayout` classes"""

    @abstractmethod
    def initialize(self, quiz_name: str, n_questions: int) -> None:
        """Initializes the quiz layout

        Args:
            quiz_name (str): Name of the quiz
            n_questions (int): Number of questions in the quiz
        """
        pass

    @abstractmethod
    def show_question(self, item: QuizItem, idx: int) -> None:
        """Update layout to show the question

        Args:
            item (QuizItem): The quiz item to be asked
            idx (int): The index of the quiz item in the quiz
        """
        pass

    @abstractmethod
    def reveal_answer(self, item: QuizItem, answer_correct: bool) -> None:
        """Update layout to show answer

        Args:
            item (QuizItem): The quiz item that was asked
            answer_correct (bool): Whether the question was answered correctly
        """
        pass

    def show_results(self, has_won: bool) -> None:
        """Update the layout to show the quiz result

        Args:
            has_won (bool): Whether the user has won
        """
        pass


@dataclass
class FancyQuizLayout(QuizLayoutBase):
    layout: Optional[Layout] = None

    def print(self):
        print(self.layout)

    def initialize(self, quiz_name: str, n_questions: int) -> None:
        self.quiz_name = quiz_name
        self.n_questions = n_questions

        if self.layout is None:
            self.layout = self._make_quiz_layout()
        self.statsbar = self._make_statsbar(n_questions)
        self.progressbar = self._make_progressbar(n_questions)

        self.layout["stats"].update(Panel(self.statsbar, title="Stats"))
        self.layout["progress"].update(Panel(self.progressbar))
        self._reset_dialog()

        print(self.layout)

    def show_question(self, item: QuizItem, idx: int) -> None:
        self._reset_answer()
        self._reset_dialog()
        self.layout["question"].update(
            Panel(
                Align.center(f"[bold]{item.question}", vertical="middle"),
                title=f"[blue]Question {idx}/{self.n_questions}[/blue] | {self.quiz_name}",
                border_style="green",
                highlight=True,
            )
        )
        print(self.layout)

    def reveal_answer(self, item: QuizItem, answer_correct: bool) -> None:
        color = "bold green" if answer_correct else "bold red"
        self.layout["answer"].update(
            Panel(
                Align.center(f"[{color}]{item.answer}", vertical="middle"),
                title=f"[blue]Answer",
                border_style="green",
                highlight=True,
            )
        )
        print(self.layout)

        if answer_correct:
            self.layout["dialog"].update(
                Panel(
                    Align.center(
                        f":fire: [{color}]That's correct! :fire: [/{color}] {motivate()}",
                        vertical="middle",
                    ),
                )
            )
            # Advance 'correct' statsbar
            self.statsbar.advance(0)
        else:
            self.layout["dialog"].update(
                Panel(
                    Align.center(
                        f"[red bold]:cross_mark: That's wrong :cross_mark: [/red bold]",
                        vertical="middle",
                    ),
                )
            )
            # Advance 'wrong' statsbar
            self.statsbar.advance(1)

        self.progressbar.advance(0)
        self.print()

    def show_results(self, has_won: Optional[bool] = None) -> None:
        if has_won is None:
            result_message = f"[blue bold]See you soon ![/blue bold]"
        elif has_won:
            result_message = f":trophy: [green bold]You won![/green bold] :trophy: See you soon, champion!"
        else:
            result_message = (
                f"[red bold]Game Over![/red bold] :disappointed_face: See you soon !"
            )

        n_correct = self.statsbar.tasks[0].completed
        n_false = self.statsbar.tasks[1].completed
        n_total = self.progressbar.tasks[0].total

        result_message += f"\nYou have answered {em(n_correct, 'green')} question(s) correctly and {em(n_false, 'red')} incorrectly"
        l = Layout(
            Panel(
                Align.center(result_message, vertical="middle"),
                title=f"[blue]Results",
            ),
        )
        print(l)

    def _reset_answer(self) -> None:
        self.layout["answer"].update(
            Panel(
                Align.center(
                    f":question-emoji::question-emoji::question-emoji:",
                    vertical="middle",
                ),
                title=f"[blue]Answer",
            )
        )

    def _reset_dialog(self) -> None:
        self.layout["dialog"].update(
            Panel(
                Align.center(
                    f"[bold blue]Type in your answer!",
                    vertical="middle",
                ),
            )
        )

    @staticmethod
    def _make_quiz_layout() -> Layout:
        layout = Layout(name="root")
        layout.split_column(
            Layout(name="progress"),
            Layout(name="question"),
            Layout(name="answer"),
            Layout(name="footer"),
        )
        layout["progress"].ratio = 2
        layout["question"].ratio = 8
        layout["answer"].ratio = 8
        layout["footer"].ratio = 3

        layout["footer"].split_row(Layout(name="dialog"), Layout(name="stats"))
        layout["dialog"].ratio = 2
        layout["stats"].ratio = 1
        return layout

    @staticmethod
    def _make_progressbar(total: int) -> Progress:
        progressbar = Progress(
            "{task.description}",
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            expand=True,
        )
        progressbar.add_task("[cyan]Quiz Progress", total=total)
        return progressbar

    @staticmethod
    def _make_statsbar(total: int) -> Progress:
        statsbar = Progress(
            "{task.description}",
            SpinnerColumn(),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        )
        statsbar.add_task("[green]Correct", total=total)
        statsbar.add_task("[red]Wrong", total=total)
        return statsbar
