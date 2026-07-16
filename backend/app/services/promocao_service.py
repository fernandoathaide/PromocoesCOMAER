"""
Service responsável pelas promoções.
"""

from datetime import date

from domain.entities.promocao import Promocao


class PromocaoService:
    """
    Regras referentes às promoções.
    """

    def promover(
        self,
        militar,
    ) -> Promocao:
        """
        Promove um militar para o próximo posto.
        """

        return Promocao(
            militar=militar,
            posto_origem=militar.posto,
            posto_destino=militar.proximo_posto,
            data=date.today(),
        )
