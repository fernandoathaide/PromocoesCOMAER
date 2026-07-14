"""
Service da entidade Militar.
"""

from __future__ import annotations

from backend.app.repositories.militar_repository import MilitarRepository
from domain.entities.militar import Militar


class MilitarService:
    """
    Camada de regras de negócio da entidade Militar.
    """

    def __init__(self):

        self.repository = MilitarRepository()

    def listar(self) -> list[Militar]:
        """
        Retorna todos os militares.
        """

        return self.repository.listar()

    def quantidade(self) -> int:
        """
        Quantidade de militares.
        """

        return self.repository.quantidade()

    def buscar(
        self,
        numero_ordem: str,
    ) -> Militar | None:
        """
        Busca um militar pelo Número de Ordem.
        """

        return self.repository.buscar_por_numero_ordem(
            numero_ordem,
        )

    def listar_por_posto(
        self,
        posto: str,
    ) -> list[Militar]:
        """
        Lista militares por posto.
        """

        return self.repository.listar_por_posto(
            posto,
        )

    def fechar(self):
        """
        Fecha a sessão do banco.
        """

        self.repository.close()
