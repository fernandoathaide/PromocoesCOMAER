"""
Service responsável pela execução da
promoção em cascata.
"""

from __future__ import annotations

from domain.entities.promocao import Promocao
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
        promocao: Promocao,
    ) -> None:
        """
        Executa um passo da cascata.

        Nesta primeira versão apenas promove
        o militar imediatamente inferior.
        """

        posto_anterior = self.cascata.posto_anterior(
            promocao.posto_origem,
        )

        if posto_anterior is None:
            return

        motor.promover_mais_antigo(
            posto_anterior.codigo.value,
            promocao.militar.quadro.codigo.value,
        )
