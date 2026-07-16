"""
Service responsável pelas promoções.
"""

from __future__ import annotations

from datetime import date

from domain.entities.indicador import Indicador
from domain.entities.militar import Militar
from domain.entities.promocao import Promocao


class PromocaoService:
    """
    Responsável por criar promoções e
    atualizar os indicadores relacionados.
    """

    def __init__(
        self,
        indicador: Indicador | None = None,
    ):

        self.indicador = indicador

    def promover(
        self,
        militar: Militar,
    ) -> Promocao:
        """
        Cria uma promoção para o militar.
        """

        proximo = militar.proximo_posto

        if proximo is None:
            raise ValueError("Militar não possui posto superior.")

        promocao = Promocao(
            militar=militar,
            posto_origem=militar.posto,
            posto_destino=proximo,
            data=date.today(),
        )

        if self.indicador is not None:
            self.indicador.registrar_promocao()

        return promocao
