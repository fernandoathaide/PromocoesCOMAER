"""
Service responsável pelo gerenciamento
das vagas da simulação.
"""

from __future__ import annotations

from domain.entities.vaga import Vaga
from domain.value_objects.posto import Posto
from domain.value_objects.quadro import Quadro


class VagaService:
    """
    Gerencia todas as vagas da simulação.
    """

    def __init__(
        self,
        indicador=None,
    ):

        self.indicador = indicador

        self._vagas: dict[
            tuple[str, str],
            Vaga,
        ] = {}

    def carregar(self):

        self._vagas.clear()

    def obter(
        self,
        posto: Posto,
        quadro: Quadro,
    ) -> Vaga | None:

        return self._vagas.get(
            (
                posto.codigo.value,
                quadro.codigo.value,
            )
        )

    def abrir(
        self,
        posto: Posto,
        quadro: Quadro,
    ) -> Vaga:

        chave = (
            posto.codigo.value,
            quadro.codigo.value,
        )

        vaga = self._vagas.get(chave)

        if vaga is None:
            vaga = Vaga(
                posto=posto,
                quadro=quadro,
                quantidade=1,
            )

            self._vagas[chave] = vaga

        else:
            vaga.liberar()

        if self.indicador is not None:
            self.indicador.abrir_vaga()

        return vaga

    def ocupar(
        self,
        posto: Posto,
        quadro: Quadro,
    ) -> bool:

        vaga = self.obter(
            posto,
            quadro,
        )

        if vaga is None:
            return False

        if not vaga.possui_vaga:
            return False

        vaga.ocupar()

        if self.indicador is not None:
            self.indicador.ocupar_vaga()

        return True

    @property
    def vagas(self):

        return list(self._vagas.values())

    @property
    def quantidade(self):

        return len(self._vagas)
