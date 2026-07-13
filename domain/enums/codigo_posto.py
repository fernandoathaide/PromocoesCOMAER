"""
Enum dos postos do COMAER.
"""

from enum import Enum


class CodigoPosto(str, Enum):
    CORONEL = "CL"
    BRIGADEIRO = "BR"
    MAJOR_BRIGADEIRO = "MB"
    TENENTE_BRIGADEIRO = "TB"
    MARECHAL_DO_AR = "MA"

    @property
    def nome(self) -> str:
        return {
            CodigoPosto.CORONEL: "Coronel",
            CodigoPosto.BRIGADEIRO: "Brigadeiro",
            CodigoPosto.MAJOR_BRIGADEIRO: "Major-Brigadeiro",
            CodigoPosto.TENENTE_BRIGADEIRO: "Tenente-Brigadeiro",
            CodigoPosto.MARECHAL_DO_AR: "Marechal do Ar",
        }[self]

    @property
    def nivel(self) -> int:
        return {
            CodigoPosto.CORONEL: 1,
            CodigoPosto.BRIGADEIRO: 2,
            CodigoPosto.MAJOR_BRIGADEIRO: 3,
            CodigoPosto.TENENTE_BRIGADEIRO: 4,
            CodigoPosto.MARECHAL_DO_AR: 5,
        }[self]

    @property
    def proximo(self):

        ordem = list(CodigoPosto)

        indice = ordem.index(self)

        if indice == len(ordem) - 1:
            return None

        return ordem[indice + 1]

    @property
    def anterior(self):

        ordem = list(CodigoPosto)

        indice = ordem.index(self)

        if indice == 0:
            return None

        return ordem[indice - 1]
