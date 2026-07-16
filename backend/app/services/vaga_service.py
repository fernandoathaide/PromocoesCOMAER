"""
Service responsável pelo gerenciamento das vagas da simulação.
"""

from __future__ import annotations

from collections import defaultdict

from domain.entities.vaga import Vaga


class VagaService:
    """
    Serviço responsável pelas vagas disponíveis.
    """

    def __init__(self):

        self._vagas = defaultdict(dict)

    def adicionar(self, vaga: Vaga):

        self._vagas[vaga.posto.codigo.value][vaga.quadro.codigo.value] = vaga

    def buscar(
        self,
        posto: str,
        quadro: str,
    ) -> Vaga | None:

        return self._vagas.get(
            posto.upper(),
            {},
        ).get(quadro.upper())

    def listar(self):

        resultado = []

        for vagas in self._vagas.values():
            resultado.extend(vagas.values())

        return resultado

    @property
    def quantidade(self) -> int:

        return len(self.listar())

    def limpar(self):

        self._vagas.clear()
