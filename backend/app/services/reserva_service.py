"""
Service responsável pelas reservas.
"""

from __future__ import annotations

from datetime import date

from domain.entities.indicador import Indicador
from domain.entities.militar import Militar
from domain.entities.reserva import Reserva


class ReservaService:
    """
    Responsável por registrar reservas
    e atualizar os indicadores.
    """

    def __init__(
        self,
        indicador: Indicador | None = None,
    ):

        self.indicador = indicador

    def registrar(
        self,
        militar: Militar,
    ) -> Reserva:
        """
        Registra a passagem do militar
        para a reserva.
        """

        reserva = Reserva(
            militar=militar,
            data=date.today(),
        )

        if self.indicador is not None:
            self.indicador.registrar_reserva()

        return reserva
