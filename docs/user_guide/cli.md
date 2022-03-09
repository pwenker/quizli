# `quizli`

Welcome to quizli

An educational project teaching how to open-source an interactive Python quiz app

Check out the project at: https://github.com/pwenker/quizli/

**Usage**:

```console
$ quizli [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `demo`: Open the documentation page in the browser
* `start`: Start the quiz with the configuration of your...

## `quizli demo`

Open the documentation page in the browser

**Usage**:

```console
$ quizli demo [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `quizli start`

Start the quiz with the configuration of your choice.

### Select Quiz Content

There are 2 ways to create a quiz with `quizli`:

1. From a csv file containing question-answer pairs: e.g. `quizli start --from-csv examples/quiz.csv`
2. From a function in the `example` module: e.g. `quizli start --quiz-name python_quiz`

### Select Quiz Settings

You can choose to

- Shuffle the quiz with the `--randomize` flag (default), or keep it `--in-order`.

- Terminate the quiz with the first wrong answer with `mode=sudden_death`, or continue on failure with `mode=complete` (default).

**Usage**:

```console
$ quizli start [OPTIONS]
```

**Options**:

* `--from-csv PATH`: Read a quiz from a csv-file
* `--mode [sudden_death|complete]`: Select the condition for the quiz to end  [default: complete]
* `--quiz-name [python_quiz|binary_number_quiz]`: Select a built-in quiz  [default: python_quiz]
* `--randomize / --in-order`: Shuffle the quiz before starting it  [default: True]
* `--help`: Show this message and exit.
