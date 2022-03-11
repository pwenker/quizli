""" 
Basic testing for the `quizli` app.

See: https://typer.tiangolo.com/tutorial/testing/
"""


import pytest
from typer.testing import CliRunner

from quizli.main import app

runner = CliRunner()


#  ╭──────────────────────────────────────────────────────────╮
#  │ Test Help Commands                                       │
#  ╰──────────────────────────────────────────────────────────╯
help_commands = [
    "--help",
    "demo --help",
    "start --help",
]


@pytest.mark.parametrize("test_input", help_commands)
def test_help_commands(
    test_input,
):
    result = runner.invoke(app, test_input)
    assert result.exit_code == 0


#  ╭──────────────────────────────────────────────────────────╮
#  │ Test Demo Command                                        │
#  ╰──────────────────────────────────────────────────────────╯
def test_demo():
    result = runner.invoke(app, "demo")
    assert result.exit_code == 0


#  ╭──────────────────────────────────────────────────────────╮
#  │ Test Start Command                                       │
#  ╰──────────────────────────────────────────────────────────╯
@pytest.mark.parametrize(
    "test_cmd, test_inp, exp_out",
    [
        (
            "start --quiz-name python_quiz",
            ["modules\n", "Answer\n", "n\n", "n\n"],
            "See you soon",
        ),
        (
            "start --quiz-name python_quiz",
            ["objects\n", "quizli\n", "Answer\n", "n\n", "n\n"],
            "See you soon",
        ),
    ],
)
def test_start_builtin_quiz(test_cmd, test_inp, exp_out):
    result = runner.invoke(app, test_cmd, input="".join(test_inp))

    assert result.exit_code == 0
    assert exp_out in result.stdout


@pytest.mark.parametrize(
    "test_cmd, test_inp, exp_out",
    [
        (
            "start --from-csv examples/quiz.csv --mode sudden_death --in-order",
            ["pip install quizli", "yes", "2", "monty python", "42", "yes", ""],
            "🏆 You won! 🏆 See you soon, champion!",
        ),
        (
            "start --from-csv examples/quiz.csv --mode sudden_death --in-order",
            ["pip install quizli", "yes", "2", "monty python", "42", "no", "n"],
            "Game Over! 😞 See you soon !",
        ),
    ],
)
def test_start_quiz_from_csv(test_cmd, test_inp, exp_out):
    result = runner.invoke(app, test_cmd, input="\n\n".join(test_inp))

    assert result.exit_code == 0
    assert exp_out in result.stdout
