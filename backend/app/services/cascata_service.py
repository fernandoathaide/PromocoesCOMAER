"""
Service responsável pela execução da
promoção em cascata.
"""

from __future__ import annotations

from domain.simulation.cascata import Cascata


class CascataService:
    """
    Executa a cascata de promoções.
    """

    def __init__(self):

        self.cascata = Cascata()

    def executar(
        self,
        motor,
        promocao,
    ) -> None:
        """
        Executa toda a cascata de promoções.

        Para cada promoção realizada,
        procura automaticamente o militar
        mais antigo do posto imediatamente
        inferior, até não existirem mais
        postos abaixo.
        """

        posto_anterior = self.cascata.posto_anterior(
            promocao.posto_origem,
        )

        if posto_anterior is None:
            return

        nova_promocao = motor.promover_mais_antigo(
            posto_anterior.codigo.value,
            promocao.militar.quadro.codigo.value,
        )

        if nova_promocao is None:
            return

        #
        # Continua a cascata
        #
        self.executar(
            motor,
            nova_promocao,
        )
