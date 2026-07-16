"""
Regras de domínio da promoção em cascata.
"""

from __future__ import annotations

from domain.value_objects.posto import Posto


class Cascata:
    """
    Contém somente regras de domínio da cascata.
    """

    def posto_anterior(
        self,
        posto: Posto,
    ) -> Posto | None:
        """
        Retorna o posto imediatamente inferior.
        """

        return posto.anterior

    def posto_superior(
        self,
        posto: Posto,
    ) -> Posto | None:
        """
        Retorna o posto imediatamente superior.
        """

        return posto.proximo

    def possui_anterior(
        self,
        posto: Posto,
    ) -> bool:

        return posto.anterior is not None

    def possui_superior(
        self,
        posto: Posto,
    ) -> bool:

        return posto.proximo is not None
