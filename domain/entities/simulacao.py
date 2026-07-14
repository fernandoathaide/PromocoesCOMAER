"""
Entity Simulação.

Representa uma execução completa da simulação de promoções.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from domain.entities.indicador import Indicador
from domain.entities.militar import Militar
from domain.entities.promocao import Promocao
from domain.entities.reserva import Reserva
from domain.entities.vaga import Vaga


@dataclass
class Simulacao:
    """
    Estado completo de uma simulação.
    """

    militares: list[Militar] = field(default_factory=list)

    vagas: list[Vaga] = field(default_factory=list)

    promocoes: list[Promocao] = field(default_factory=list)

    reservas: list[Reserva] = field(default_factory=list)

    indicadores: Indicador = field(default_factory=Indicador)

    #
    # Militares
    #

    def adicionar_militar(
        self,
        militar: Militar,
    ) -> None:

        self.militares.append(militar)

    @property
    def quantidade_militares(self) -> int:

        return len(self.militares)

    #
    # Vagas
    #

    def adicionar_vaga(
        self,
        vaga: Vaga,
    ) -> None:

        self.vagas.append(vaga)

    @property
    def quantidade_vagas(self) -> int:

        return len(self.vagas)

    #
    # Promoções
    #

    def adicionar_promocao(
        self,
        promocao: Promocao,
    ) -> None:

        self.promocoes.append(promocao)

    @property
    def quantidade_promocoes(self) -> int:

        return len(self.promocoes)

    #
    # Reservas
    #

    def adicionar_reserva(
        self,
        reserva: Reserva,
    ) -> None:

        self.reservas.append(reserva)

    @property
    def quantidade_reservas(self) -> int:

        return len(self.reservas)

    #
    # Estatísticas
    #

    @property
    def militares_ativos(self) -> list[Militar]:

        return [militar for militar in self.militares if militar.esta_na_ativa]

    @property
    def militares_reserva(self) -> list[Militar]:

        return [militar for militar in self.militares if militar.esta_na_reserva]

    def limpar(self) -> None:
        """
        Reinicia completamente a simulação.
        """

        self.militares.clear()
        self.vagas.clear()
        self.promocoes.clear()
        self.reservas.clear()

        self.indicadores = Indicador()

    def __str__(self) -> str:

        return (
            f"Simulação("
            f"militares={self.quantidade_militares}, "
            f"vagas={self.quantidade_vagas}, "
            f"promoções={self.quantidade_promocoes}, "
            f"reservas={self.quantidade_reservas})"
        )

    def __repr__(self) -> str:

        return (
            "Simulacao("
            f"militares={self.quantidade_militares}, "
            f"vagas={self.quantidade_vagas}, "
            f"promocoes={self.quantidade_promocoes}, "
            f"reservas={self.quantidade_reservas})"
        )
