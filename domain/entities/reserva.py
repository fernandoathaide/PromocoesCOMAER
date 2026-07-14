"""
Entity Reserva.

Representa a passagem de um militar para a reserva.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from domain.entities.militar import Militar


@dataclass(frozen=True)
class Reserva:
    """
    Evento de passagem para a reserva.
    """

    militar: Militar

    data: date

    motivo: str = "RESERVA"

    @property
    def numero_ordem(self) -> str:
        return str(self.militar.numero_ordem)

    @property
    def posto(self):
        return self.militar.posto

    @property
    def quadro(self):
        return self.militar.quadro

    @property
    def nome_guerra(self) -> str:
        return self.militar.nome_guerra

    @property
    def descricao(self) -> str:
        return f"{self.nome_guerra} passou para a reserva como {self.posto.nome}"

    def __str__(self) -> str:
        return self.descricao

    def __repr__(self) -> str:
        return (
            "Reserva("
            f"numero_ordem='{self.numero_ordem}', "
            f"posto='{self.posto.codigo.value}', "
            f"quadro='{self.quadro.codigo.value}'"
            ")"
        )
