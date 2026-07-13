"""
Value Object Posto.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import cast

from domain.enums.codigo_posto import CodigoPosto


@dataclass(frozen=True)
class Posto:
    """
    Value Object que representa um posto militar.
    """

    codigo: CodigoPosto | str

    def __post_init__(self):

        if isinstance(self.codigo, str):
            object.__setattr__(
                self,
                "codigo",
                CodigoPosto(self.codigo.upper()),
            )

    @property
    def enum(self) -> CodigoPosto:
        return cast(CodigoPosto, self.codigo)

    @property
    def nome(self) -> str:
        return self.enum.nome

    @property
    def nivel(self) -> int:
        return self.enum.nivel

    @property
    def proximo(self) -> "Posto | None":

        codigo = self.enum.proximo

        if codigo is None:
            return None

        return Posto(codigo)

    @property
    def anterior(self) -> "Posto | None":

        codigo = self.enum.anterior

        if codigo is None:
            return None

        return Posto(codigo)

    @property
    def eh_coronel(self) -> bool:
        return self.enum is CodigoPosto.CORONEL

    @property
    def eh_brigadeiro(self) -> bool:
        return self.enum is CodigoPosto.BRIGADEIRO

    @property
    def eh_major_brigadeiro(self) -> bool:
        return self.enum is CodigoPosto.MAJOR_BRIGADEIRO

    @property
    def eh_tenente_brigadeiro(self) -> bool:
        return self.enum is CodigoPosto.TENENTE_BRIGADEIRO

    @property
    def eh_marechal(self) -> bool:
        return self.enum is CodigoPosto.MARECHAL_DO_AR

    def __lt__(self, other: "Posto") -> bool:
        return self.nivel < other.nivel

    def __le__(self, other: "Posto") -> bool:
        return self.nivel <= other.nivel

    def __gt__(self, other: "Posto") -> bool:
        return self.nivel > other.nivel

    def __ge__(self, other: "Posto") -> bool:
        return self.nivel >= other.nivel

    def __str__(self) -> str:
        return self.nome

    def __repr__(self) -> str:
        return f"Posto({self.enum.value})"
