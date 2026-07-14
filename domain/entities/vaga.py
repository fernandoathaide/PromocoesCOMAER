"""
Entity Vaga.

Representa uma vaga de promoção de determinado
posto e quadro.
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.value_objects.posto import Posto
from domain.value_objects.quadro import Quadro


@dataclass
class Vaga:
    """
    Representa uma vaga disponível para promoção.
    """

    posto: Posto

    quadro: Quadro

    quantidade: int = 0

    @property
    def possui_vaga(self) -> bool:
        """
        Indica se ainda existe vaga disponível.
        """

        return self.quantidade > 0

    @property
    def esta_esgotada(self) -> bool:
        """
        Indica se todas as vagas foram ocupadas.
        """

        return self.quantidade == 0

    def ocupar(self) -> None:
        """
        Consome uma vaga.
        """

        if self.quantidade <= 0:
            raise ValueError("Não existem vagas disponíveis.")

        self.quantidade -= 1

    def liberar(self) -> None:
        """
        Adiciona uma vaga.
        """

        self.quantidade += 1

    def __str__(self) -> str:
        return f"{self.posto} - {self.quadro.codigo.value} ({self.quantidade} vagas)"

    def __repr__(self) -> str:
        return (
            "Vaga("
            f"posto='{self.posto.codigo.value}', "
            f"quadro='{self.quadro.codigo.value}', "
            f"quantidade={self.quantidade}"
            ")"
        )
