"""
Motor principal da Simulação.

Responsável por carregar os militares e
organizar as estruturas utilizadas pelo
algoritmo de promoções.
"""

from __future__ import annotations

from collections import defaultdict

from backend.app.repositories.militar_repository import MilitarRepository
from backend.app.services.promocao_service import PromocaoService
from domain.entities.simulacao import Simulacao


class MotorSimulacao:
    """
    Motor principal da simulação.
    """

    def __init__(self):

        self.repository = MilitarRepository()

        self.promocao_service = PromocaoService()

        self.simulacao = Simulacao()

        self._por_posto = defaultdict(list)

        self._por_quadro = defaultdict(list)

        self._por_posto_quadro = defaultdict(list)

    def carregar(self) -> Simulacao:
        """
        Carrega todos os militares da RAW
        e cria os índices necessários para
        o algoritmo de simulação.
        """
        self._por_posto.clear()
        self._por_quadro.clear()
        self._por_posto_quadro.clear()

        self.simulacao = Simulacao()

        militares = self.repository.listar()

        for militar in militares:
            self.simulacao.adicionar_militar(militar)

            self._por_posto[militar.posto.codigo.value].append(militar)

            self._por_quadro[militar.quadro.codigo.value].append(militar)

            self._por_posto_quadro[
                (
                    militar.posto.codigo.value,
                    militar.quadro.codigo.value,
                )
            ].append(militar)

        return self.simulacao

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

    def promover(
        self,
        militar,
    ):
        """
        Executa a promoção de um militar.
        o resultado na simulação.
        """

        promocao = self.promocao_service.promover(
            militar,
        )

        self.simulacao.adicionar_promocao(
            promocao,
        )

        return promocao

    @property
    def quantidade_promocoes(self):
        """
        Retorna a quantidade de promoções
        registradas na simulação.
        """

        return self.simulacao.quantidade_promocoes

    def promover_mais_antigo(
        self,
        posto: str,
        quadro: str,
    ):
        """
        Promove o militar mais antigo de um
        determinado posto e quadro.
        """

        militares = self.militares(
            posto,
            quadro,
        )

        if not militares:
            return None

        militar = min(
            militares,
            key=lambda m: m.antiguidade.inteiro,
        )

        return self.promover(
            militar,
        )

    def fechar(self):

        self.repository.close()
