"""
Service responsável pelas promoções.
"""

from __future__ import annotations

from datetime import date

from domain.entities.militar import Militar
from domain.entities.promocao import Promocao


class PromocaoService:
    """
    Serviço responsável pelas promoções militares.
    """

    def promover(
        self,
        militar: Militar,
    ) -> Promocao:
        """
        Promove um militar para o posto imediatamente superior.
        """

        novo = militar.promover()

        return Promocao(
            militar=novo,
            posto_origem=militar.posto,
            posto_destino=novo.posto,
            data=date.today(),
        )
