"""
Value Object - Antiguidade.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Antiguidade:
    """
    Representa a posição de antiguidade do militar.
    """

    valor: str

    def __post_init__(self):

        numero = str(self.valor).strip()

        if not numero:
            raise ValueError("Antiguidade não pode ser vazia.")

        if not numero.isdigit():
            raise ValueError("Antiguidade deve conter apenas números.")

        object.__setattr__(
            self,
            "valor",
            numero.zfill(8),
        )

    @property
    def inteiro(self) -> int:
        return int(self.valor)

    def __int__(self):
        return self.inteiro

    def __lt__(self, other: "Antiguidade"):
        return self.inteiro < other.inteiro

    def __le__(self, other: "Antiguidade"):
        return self.inteiro <= other.inteiro

    def __gt__(self, other: "Antiguidade"):
        return self.inteiro > other.inteiro

    def __ge__(self, other: "Antiguidade"):
        return self.inteiro >= other.inteiro

    def __str__(self):
        return self.valor

    def __repr__(self):
        return f"Antiguidade('{self.valor}')"
