"""
Value Object - Número de Ordem (SARAM).

Representa o identificador único de um militar no COMAER.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NumeroOrdem:
    """
    Identificador único do militar.
    """

    valor: str

    def __post_init__(self):

        numero = str(self.valor).strip()

        if not numero:
            raise ValueError("Número de Ordem não pode ser vazio.")

        object.__setattr__(self, "valor", numero)

    @property
    def inteiro(self) -> int:
        """
        Retorna o Número de Ordem como inteiro.
        """

        return int(self.valor)

    def __int__(self) -> int:
        return self.inteiro

    def __str__(self) -> str:
        return self.valor

    def __repr__(self) -> str:
        return f"NumeroOrdem('{self.valor}')"
