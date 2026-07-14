"""
Entity Promoção.

Representa um evento de promoção de um militar.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from domain.entities.militar import Militar
from domain.value_objects.posto import Posto


@dataclass(frozen=True)
class Promocao:
    """
    Representa uma promoção de posto.
    """

    militar: Militar

    posto_origem: Posto

    posto_destino: Posto

    data: date

    motivo: str = "SIMULAÇÃO"

    @property
    def nome_guerra(self) -> str:
        return self.militar.nome_guerra

    @property
    def numero_ordem(self) -> str:
        return str(self.militar.numero_ordem)

    @property
    def descricao(self) -> str:
        return f"{self.nome_guerra}: {self.posto_origem.nome} → {self.posto_destino.nome}"

    @property
    def houve_promocao(self) -> bool:
        return self.posto_origem != self.posto_destino

    def __str__(self) -> str:
        return self.descricao

    def __repr__(self) -> str:
        return (
            "Promocao("
            f"numero_ordem='{self.numero_ordem}', "
            f"origem='{self.posto_origem.codigo.value}', "
            f"destino='{self.posto_destino.codigo.value}'"
            ")"
        )
