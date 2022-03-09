"""
This module contains the entrypoint to quizli.

We use the `typer` package to create a CLI.

For more information see the [CLI reference](pwenker.github.io/quizli/user_guide/cli.html)
"""


from pathlib import Path
from typing import Optional

import typer
from rich import print

from quizli import Quiz, QuizConfig, QuizMode, examples
from quizli.examples import QuizKind
from quizli.session import QuizSession

# {==(1)==} Here, we define our CLI app and give it a short but informative description
# This will be shown on top of the help text when the app is launched with
# `quizli --help`.

app = typer.Typer(
    help="""Welcome to quizli
    
    An educational project teaching how to open-source an interactive Python quiz app
    
    Check out the project at: https://github.com/pwenker/quizli/
    """
)

# {==(2)==} The `@app.command` decorator turns the function into a command for our CLI.
# This way, the user can launch the `demo`-function with `quizli demo`
# Here, as a result, the demo section of the docs will be opened in a new browser tab.
@app.command()
def demo():
    """Open the documentation page in the browser"""
    import webbrowser

    webbrowser.open("https://pwenker.github.io/quizli/demos.html", new=2)


# {==(3)==} Again, we define a command for our CLI: `quizli start`.
# This time, we add a lot of parameters to the function, which will be translated
# into CLI options. Here, Typer will make use of the type hints we provide.
# For example, by supplying the `QuizKind` enumeration type hint to the
# `quiz_name` parameter, Typer will automatically check that the user supplies a
# valid variant when running the command: `quizli start --quiz-name <quiz-name>`
# and it will show all existing variants in the help message `quizli start --help`.
@app.command()
def start(
    from_csv: Optional[Path] = typer.Option(
        None, exists=True, help="Read a quiz from a csv-file"
    ),
    mode: QuizMode = typer.Option(
        QuizMode.COMPLETE,
        help="Select the condition for the quiz to end",
    ),
    quiz_name: QuizKind = typer.Option(
        QuizKind.PYTHON_QUIZ, help="Select a built-in quiz"
    ),
    randomize: bool = typer.Option(
        True,
        "--randomize/--in-order",
        help="Shuffle the quiz before starting it",
    ),
):
    # {==(4)==} The docstring below will automatically be inserted into the help message
    # and can be shown with `quizli start --help`. The same is true for the help
    # strings we defined above for the parameters of the `start` function.
    """
    Start the quiz with the configuration of your choice.

    ### Select Quiz Content

    There are 2 ways to create a quiz with `quizli`:

    1. From a csv file containing question-answer pairs: e.g. `quizli start --from-csv examples/quiz.csv`
    2. From a function in the `example` module: e.g. `quizli start --quiz-name python_quiz`

    ### Select Quiz Settings

    You can choose to

    - Shuffle the quiz with the `--randomize` flag (default), or keep it `--in-order`.

    - Terminate the quiz with the first wrong answer with `mode=sudden_death`, or continue on failure with `mode=complete` (default).
    """

    config = QuizConfig(mode=mode, randomize=randomize)

    if from_csv is not None:
        quiz = Quiz.from_csv(Path(from_csv))
    else:
        quiz = getattr(examples, quiz_name)()

    quiz_session = QuizSession(quiz, config)
    quiz_session.start()


if __name__ == "__main__":
    app()
