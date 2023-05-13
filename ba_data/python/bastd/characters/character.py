"""Module for exporting character types and models."""

from __future__ import annotations

from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from enum import Enum

from bastd.actor import spaz as spz

if TYPE_CHECKING:
    from typing import Any, Type


CHARACTERS: dict[str, Type[Character]] = {}


class Characters(Enum):
    """List of characters."""

    KRONK = "Kronk"
    ZOE = "Zoe"
    JACKMORGAN = "Jack Morgan"
    MEL = "Mel"
    SNAKESHADOW = "Snake Shadow"
    BONES = "Bones"
    BERNARD = "Bernard"
    WIZARD = "Grumbledorf"
    PASCAL = "Pascal"
    FROSTY = "Frosty"
    CYBORG = "B-9000"
    PIXIE = "Pixel"
    AGENT = "Agent Johnson"
    TAOBAOMASCOT = "Taobao Mascot"
    SANTA = "Santa Claus"
    BUNNY = "Easter Bunny"


def register_character(character: Characters, cls: Type[Character]) -> None:
    """Registers the given class of the modified character.

    Parameters
    ----------
    character : name of the character
        Stricty use the `Characters` Enum.
    cls : class name
        This class should be inherited from abstract class `character.Character`.
    """
    CHARACTERS[character.value] = cls


class Character(ABC):
    """Character class represeting the spaz."""

    @abstractmethod
    def modify_spaz(self, spaz: spz.Spaz) -> None:
        """
        Entrypoint for modyfing any character.

        This method will automatically revice the current
        instace of spaz as the first argument.
        """

    @abstractmethod
    def handlemessage(self, msg: Any) -> None:
        """
        Handle the messages sent by spaz.

        This method will be helpfull to handle our custom
        inputs to triger certain abilities.
        """


# keeping these here for any possible future use and keeping game code seprate


def handle_spaz(spaz: spz.Spaz) -> None:
    """Entrypoint of spaz. Handles the newly spawned character."""

    char = CHARACTERS.get(spaz.character_name)

    if spaz.character_name not in CHARACTERS:
        return

    if char is not None:
        setattr(spaz, "character", char())
        spaz.character.modify_spaz(spaz)  # type: ignore


def handle_inputs(spaz: spz.Spaz, msg: Any) -> None:
    """
    Entrypoint of messages for our spaz. This will be
    usefull to recive our custom input messages.
    """
    if hasattr(spaz, "character"):
        spaz.character.handlemessage(msg)  # type: ignore
