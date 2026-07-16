"""
Motor principal da Simulação.

Responsável por carregar os militares e
organizar as estruturas utilizadas pelo
algoritmo de promoções.
"""

from __future__ import annotations

from collections import defaultdict

from backend.app.repositories.militar_repository import MilitarRepository
from domain.entities.simulacao import Simulacao


class MotorSimulacao:
    """
    Motor principal da simulação.
    """

    def __init__(self):

        self.repository = MilitarRepository()

        self._por_posto = defaultdict(list)

        self._por_quadro = defaultdict(list)

        self._por_posto_quadro = defaultdict(list)

    def carregar(self) -> Simulacao:
        """
        Carrega todos os militares da RAW
        e cria os índices necessários para
        o algoritmo de simulação.
        """

        simulacao = Simulacao()

        militares = self.repository.listar()

        for militar in militares:
            simulacao.adicionar_militar(militar)

            self._por_posto[militar.posto.codigo.value].append(militar)

            self._por_quadro[militar.quadro.codigo.value].append(militar)

            self._por_posto_quadro[
                (
                    militar.posto.codigo.value,
                    militar.quadro.codigo.value,
                )
            ].append(militar)

        return simulacao

    def militares_do_posto(
        self,
        posto: str,
    ):

        return self._por_posto[posto.upper()]

    def militares_do_quadro(
        self,
        quadro: str,
    ):

        return self._por_quadro[quadro.upper()]

    def militares(
        self,
        posto: str,
        quadro: str,
    ):

        return self._por_posto_quadro[
            (
                posto.upper(),
                quadro.upper(),
            )
        ]

    def fechar(self):

        self.repository.close()
