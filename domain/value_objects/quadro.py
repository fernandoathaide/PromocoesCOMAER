"""
Value Object Quadro.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import cast

from domain.enums.codigo_quadro import CodigoQuadro


@dataclass(frozen=True)
class Quadro:
    """
    Value Object que representa um Quadro Militar.
    """

    codigo: CodigoQuadro | str

    def __post_init__(self):

        if isinstance(self.codigo, str):
            object.__setattr__(
                self,
                "codigo",
                CodigoQuadro(self.codigo.upper()),
            )

    @property
    def enum(self) -> CodigoQuadro:
        return cast(CodigoQuadro, self.codigo)

    @property
    def descricao(self) -> str:
        return self.enum.descricao

    def __str__(self) -> str:
        return self.descricao

    def __repr__(self) -> str:
        return f"Quadro({self.enum.value})"
