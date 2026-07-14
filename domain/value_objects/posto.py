"""
Value Object - Posto Militar.
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.enums.codigo_posto import CodigoPosto


@dataclass(frozen=True)
class Posto:
    """
    Representa um posto militar do COMAER.
    """

    codigo: CodigoPosto

    _POSTOS = {
        CodigoPosto.CORONEL: {
            "nome": "Coronel",
            "nivel": 1,
        },
        CodigoPosto.BRIGADEIRO: {
            "nome": "Brigadeiro",
            "nivel": 2,
        },
        CodigoPosto.MAJOR_BRIGADEIRO: {
            "nome": "Major-Brigadeiro",
            "nivel": 3,
        },
        CodigoPosto.TENENTE_BRIGADEIRO: {
            "nome": "Tenente-Brigadeiro",
            "nivel": 4,
        },
        CodigoPosto.MARECHAL_DO_AR: {
            "nome": "Marechal do Ar",
            "nivel": 5,
        },
    }

    @classmethod
    def from_codigo(cls, codigo: str) -> "Posto":
        """
        Cria um Posto a partir do código textual.
        """

        return cls(CodigoPosto(codigo.upper().strip()))

    @property
    def nome(self) -> str:
        return self._POSTOS[self.codigo]["nome"]

    @property
    def nivel(self) -> int:
        return self._POSTOS[self.codigo]["nivel"]

    @property
    def proximo(self) -> "Posto | None":

        for codigo, dados in self._POSTOS.items():
            if dados["nivel"] == self.nivel + 1:
                return Posto(codigo)

        return None

    @property
    def anterior(self) -> "Posto | None":

        for codigo, dados in self._POSTOS.items():
            if dados["nivel"] == self.nivel - 1:
                return Posto(codigo)

        return None

    @property
    def eh_coronel(self) -> bool:
        return self.codigo is CodigoPosto.CORONEL

    @property
    def eh_brigadeiro(self) -> bool:
        return self.codigo is CodigoPosto.BRIGADEIRO

    @property
    def eh_major_brigadeiro(self) -> bool:
        return self.codigo is CodigoPosto.MAJOR_BRIGADEIRO

    @property
    def eh_tenente_brigadeiro(self) -> bool:
        return self.codigo is CodigoPosto.TENENTE_BRIGADEIRO

    @property
    def eh_marechal(self) -> bool:
        return self.codigo is CodigoPosto.MARECHAL_DO_AR

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
        return f"Posto(codigo='{self.codigo.value}', nome='{self.nome}')"
