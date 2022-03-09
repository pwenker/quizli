# How to create an interactive quiz app with Python?


Since the main purpose of this learning guide is to teach you how to create an open source project for an _existing_ application or library,
we will only shortly list the main building blocks of `quizli's` code along with assignments and recommended references.

## 1. Main building blocks of a simple quiz app
!!! note "Assignment 1" 

    - a) Read through the code reference of the [`quiz` module](../code_reference/quiz.md)
    - b) Take a look at the exemplary jupyter notebook about [creating a simple quiz](../notebooks/quizli.ipynb)

!!! info "Resources" 

    - Dataclasses: [PEP-557](https://www.python.org/dev/peps/pep-0557/) & [Section in Python Docs](https://docs.python.org/3/library/dataclasses.html)

## 2. Make your quiz beautiful and interactive

In order to bring color and interactivity into our quiz we make heavy use of the [`rich`](https://github.com/Textualize/rich) library.

!!! note "Assignment 2" 
    - a) Read through the code reference of the [`layout` module](../code_reference/layout.md) and the [`session` module](../code_reference/session.md)
    - b) :material-powershell: Create your own quiz layout class that inherits from `QuizLayoutBase`, similar to the `FancyQuizLayout`. It could be a minimalist quiz layout, or maybe you want to show off your creative power and design a beautiful und super-complex layout.
    
!!! info "Resources" 

    - Read through the following sections of the `rich` documentation: 
        - [Introduction](https://rich.readthedocs.io/en/latest/introduction.html)
        - [Layouts](https://rich.readthedocs.io/en/latest/layout.html)
        - [Prompts](https://rich.readthedocs.io/en/latest/prompt.html)
        
## 2. Dynamically create a quiz 

The `examples` module shows how to dynamically create a quiz and have it automatically pop up in quizli's CLI.

!!! note "Assignment 3" 
    - a) Read through the code reference of the [`example` module](../code_reference/examples.md)
    - b) :material-powershell: Create your own dynamic quiz, by implementing a function similar to the `python_quiz` and the `binary_number_quiz` functions. Add your quiz as a variant to the `QuizKind` enumeration, so that it will be automatically added as an option in quizli's CLI.
    - c) :material-powershell: The built-in Python quiz has a problem: when asking for the name of a Python object/module given it's description, the description sometimes contains the answer itself. Improve the `python_quiz` by writing code that strips out the answer from the question field before showing it.
