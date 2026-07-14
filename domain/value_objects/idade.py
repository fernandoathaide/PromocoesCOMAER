"""
Value Object - Idade.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Idade:
    """
    Representa a idade do militar.
    """

    nascimento: date

    @property
    def anos(self) -> int:

        hoje = date.today()

        idade = hoje.year - self.nascimento.year

        if (hoje.month, hoje.day) < (self.nascimento.month, self.nascimento.day):
            idade -= 1

        return idade

    @property
    def meses(self) -> int:

        hoje = date.today()

        meses = (hoje.year - self.nascimento.year) * 12 + hoje.month - self.nascimento.month

        if hoje.day < self.nascimento.day:
            meses -= 1

        return meses

    @property
    def dias(self) -> int:

        return (date.today() - self.nascimento).days

    @property
    def maior_idade(self) -> bool:

        return self.anos >= 18

    def __int__(self):

        return self.anos

    def __str__(self):

        return f"{self.anos} anos"

    def __repr__(self):

        return f"Idade(nascimento={self.nascimento.isoformat()})"
