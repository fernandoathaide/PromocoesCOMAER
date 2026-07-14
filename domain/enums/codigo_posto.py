"""
Enum dos códigos dos postos do COMAER.

Este Enum contém apenas os códigos oficiais dos postos.
Toda a inteligência de negócio permanece no Value Object Posto.
"""

from enum import Enum


class CodigoPosto(str, Enum):
    CORONEL = "CL"

    BRIGADEIRO = "BR"

    MAJOR_BRIGADEIRO = "MB"

    TENENTE_BRIGADEIRO = "TB"

    MARECHAL_DO_AR = "MA"
