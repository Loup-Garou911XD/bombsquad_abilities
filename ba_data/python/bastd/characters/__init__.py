"""Package regarding the Character Special Abilities of the game Bombsquad."""

# ba_meta require api 7

__version__ = "0.0.2"
__all__ = ["Character", "Characters", "register_character"]


from .character import Character, Characters, register_character


# Initialize our modified characters
from . import modified
