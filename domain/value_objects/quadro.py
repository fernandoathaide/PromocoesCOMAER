"""
Value Object - Quadro Militar.
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.enums.codigo_quadro import CodigoQuadro


@dataclass(frozen=True)
class Quadro:
    """
    Representa um quadro militar do COMAER.
    """

    codigo: CodigoQuadro

    @classmethod
    def from_sig(cls, codigo: str) -> "Quadro":
        """
        Cria um Quadro a partir do código existente no SIG.
        """
        return cls(CodigoQuadro(codigo.upper().strip()))

    @property
    def descricao(self) -> str:
        return self.codigo.descricao

    def __str__(self) -> str:
        return self.descricao

    def __repr__(self) -> str:
        return f"Quadro('{self.codigo.value}')"
