"""
This module contains some utility functions
"""

import random
from typing import Union

__all__ = ["em", "motivate"]


def em(message: Union[str, int, float], col: str = "blue") -> str:
    """Emphasize a message string with markup

    Args:
        message (Union[str, int, float]): The message string
        col (str): The color of the message

    Returns:
        message in markup
    """

    return f"[{col} bold]{message}[/{col} bold]"


def motivate() -> str:
    """Return random motivational text & emoji

    This function randomly choses a motivational text along with a motivational emoji
    to be shown in the quiz layout whenever the user answers correctly.

    Returns:
        str: The motivational text + emoji
    """
    motivational_texts = [
        "So good...keep going!",
        "You are amazing!",
        "How do you do that?",
        "Just....unbelievable!",
        "Do you quiz professionally?",
        "You are unstoppable!",
        "You are on fire!",
        "Legen....wait for it....dary!",
        "Alright, I need to ask harder questions...",
        "Perfect!",
        "You are unbeatable",
        "And now for something completely different...",
    ]

    motivational_emojis = [
        ":exploding_head:" ":fire:",
        ":rocket:",
        ":exclamation_mark:",
        ":brain:",
        ":direct_hit:",
        ":flexed_biceps:",
        ":mechanical_arm:",
        ":party_popper:",
        ":partying_face:",
        ":rainbow:",
        ":sparkles:",
        ":sunglasses:",
    ]
    return f"{random.choice(motivational_texts)} {random.choice(motivational_emojis)}"
