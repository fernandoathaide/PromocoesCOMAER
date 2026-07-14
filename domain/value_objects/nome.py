"""
Value Object - Nome do Militar.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Nome:
    """
    Representa o nome completo e o nome de guerra do militar.
    """

    completo: str
    guerra: str

    def __post_init__(self):

        completo = self.completo.strip().upper()
        guerra = self.guerra.strip().upper()

        if not completo:
            raise ValueError("Nome completo não pode ser vazio.")

        if not guerra:
            raise ValueError("Nome de guerra não pode ser vazio.")

        object.__setattr__(self, "completo", completo)
        object.__setattr__(self, "guerra", guerra)

    @property
    def primeiro_nome(self) -> str:
        return self.completo.split()[0]

    @property
    def ultimo_nome(self) -> str:
        return self.completo.split()[-1]

    @property
    def tamanho(self) -> int:
        return len(self.completo)

    def contem(self, texto: str) -> bool:
        return texto.upper() in self.completo

    def __str__(self) -> str:
        return self.guerra

    def __repr__(self) -> str:
        return f"Nome(guerra='{self.guerra}', completo='{self.completo}')"
