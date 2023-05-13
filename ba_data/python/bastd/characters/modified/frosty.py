"""Special abilities for character: Frosty."""

# ba_meta require api 7

from __future__ import annotations

from typing import TYPE_CHECKING

from bastd.actor import spaz as spz
from bastd.characters.character import register_character, Characters, Character
from bastd.characters.inputs import DoubleJumpMessage

if TYPE_CHECKING:
    from typing import Any


# pylint: disable=missing-function-docstring
# NOTE: this is not true ability


class Frosty(Character):
    """Freezy Wissy"""

    def modify_spaz(self, spaz: spz.Spaz) -> None:
        spaz.bomb_type = "ice"

    def handlemessage(self, msg: Any) -> None:
        if isinstance(msg, DoubleJumpMessage):
            print("we double jumped.")


# register our modified character
register_character(Characters.FROSTY, Frosty)
