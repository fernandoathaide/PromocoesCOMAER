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

    @classmethod
    def from_sig(cls, codigo: str) -> "Posto":
        """
        Cria um Posto a partir do código existente na base SIG.
        Ex.: CL, BR, MB...
        """
        return cls(CodigoPosto(codigo.upper().strip()))

    @property
    def nome(self) -> str:
        return self.codigo.nome

    @property
    def nivel(self) -> int:
        return self.codigo.nivel

    @property
    def proximo(self) -> "Posto | None":

        if self.codigo.proximo is None:
            return None

        return Posto(self.codigo.proximo)

    @property
    def anterior(self) -> "Posto | None":

        if self.codigo.anterior is None:
            return None

        return Posto(self.codigo.anterior)

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
        return f"Posto('{self.codigo.value}')"
