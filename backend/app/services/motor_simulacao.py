"""
Motor principal da Simulação.

Responsável por executar todo o processo
de promoções do COMAER.
"""

from __future__ import annotations

from backend.app.repositories.militar_repository import MilitarRepository
from domain.entities.simulacao import Simulacao


class MotorSimulacao:
    """
    Motor principal da simulação.
    """

    def __init__(self):

        self.repository = MilitarRepository()

    def carregar(self) -> Simulacao:
        """
        Carrega todos os militares da camada RAW.
        """

        simulacao = Simulacao()

        militares = self.repository.listar()

        for militar in militares:
            simulacao.adicionar_militar(militar)

        return simulacao

    def fechar(self):

        self.repository.close()
