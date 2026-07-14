"""
Value Object - Tempo de Serviço.
"""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class TempoServico:
    """
    Representa o tempo de serviço do militar.

    Exemplo Oracle:

    32 A 06 M 05 D
    """

    texto: str

    def __post_init__(self):

        texto = self.texto.strip().upper()

        regex = r"(\d+)\s*A\s*(\d+)\s*M\s*(\d+)\s*D"

        match = re.fullmatch(regex, texto)

        if match is None:
            raise ValueError(f"Tempo de serviço inválido: {texto}")

        anos, meses, dias = map(int, match.groups())

        object.__setattr__(self, "texto", texto)
        object.__setattr__(self, "_anos", anos)
        object.__setattr__(self, "_meses", meses)
        object.__setattr__(self, "_dias", dias)

    @property
    def anos(self) -> int:
        return self._anos

    @property
    def meses(self) -> int:
        return self._meses

    @property
    def dias(self) -> int:
        return self._dias

    @property
    def total_meses(self) -> int:
        return self.anos * 12 + self.meses

    @property
    def total_dias(self) -> int:
        """
        Aproximação suficiente para comparações.
        """

        return self.anos * 365 + self.meses * 30 + self.dias

    def __lt__(self, other: "TempoServico"):
        return self.total_dias < other.total_dias

    def __le__(self, other: "TempoServico"):
        return self.total_dias <= other.total_dias

    def __gt__(self, other: "TempoServico"):
        return self.total_dias > other.total_dias

    def __ge__(self, other: "TempoServico"):
        return self.total_dias >= other.total_dias

    def __str__(self):

        return f"{self.anos} anos, {self.meses} meses e {self.dias} dias"

    def __repr__(self):

        return f"TempoServico({self.texto})"
