"""
This module contains all the necessary logic to create quiz sessions
"""


from dataclasses import dataclass

from rich import print
from rich.prompt import Confirm

from quizli import Quiz, QuizConfig, QuizMode
from quizli.layout import FancyQuizLayout

__all__ = ["QuizSession"]


@dataclass
class QuizSession:
    """This class makes a quiz interactive

    It accepts a `quiz` (`Quiz`) and interactively renders it within a `layout` (`QuizLayout`)
    to interactively ask the user questions according to a `config` (`QuizConfig`).


    Attributes:
        quiz: Determines the quiz to be started
        config: Determines the quiz settings
        layout: Determines how the quiz will look like
    """

    quiz: Quiz
    config: QuizConfig
    layout: FancyQuizLayout = FancyQuizLayout()

    def _initialize(self) -> None:
        """Apply some of the quiz settings and initialize the quiz layout"""
        if self.config.randomize:
            self.quiz.shuffle()

        self.layout.initialize(quiz_name=self.quiz.name, n_questions=len(self.quiz))

    def start(self) -> None:
        """Start the quiz

        This method powers the whole interactivity of the quiz, managing
        layout updates, as well as iterating through the quiz to ask questions.
        """
        self._initialize()

        print(self.layout.layout)

        for i, item in enumerate(self.quiz.items, start=1):

            self.layout.show_question(item=item, idx=i)

            answer_correct = item.ask(show_question=False)

            self.layout.reveal_answer(item, answer_correct=answer_correct)

            if not answer_correct and self.config.mode == QuizMode.SUDDEN_DEATH:
                self.start() if Confirm.ask(
                    "Retry the quiz?"
                ) else self.layout.show_results(has_won=False)
                return
            else:
                if not Confirm.ask("Continue", default="y"):
                    self.start() if Confirm.ask(
                        "Restart the quiz?"
                    ) else self.layout.show_results()
                    return

        if self.config.mode == QuizMode.SUDDEN_DEATH:
            self.layout.show_results(has_won=True)
        else:
            self.layout.show_results()
