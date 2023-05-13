"""Input handling for the modified spazes and abilities."""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    pass


@dataclass
class DoubleJumpMessage:
    """Spaz has double jumped."""


@dataclass
class DoublePunchMessage:
    """Spaz has double punched."""


@dataclass
class DoublePickupMessage:
    """Spaz has double pickuped."""
