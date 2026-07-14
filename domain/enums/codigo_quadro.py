"""
Enum dos códigos dos Quadros do COMAER.

Contém apenas os códigos oficiais.
Toda a inteligência permanece no Value Object Quadro.
"""

from enum import Enum


class CodigoQuadro(str, Enum):
    QOAV = "QOAV"

    QOINT = "QOINT"

    QOMED = "QOMED"

    QODENT = "QODENT"

    QOFARM = "QOFARM"

    QOINF = "QOINF"

    QOENG = "QOENG"

    QOCAPL = "QOCAPL"

    QOEARM = "QOEARM"

    QOEAV = "QOEAV"

    QOECOM = "QOECOM"

    QOECTA = "QOECTA"

    QOEFOT = "QOEFOT"

    QOEMET = "QOEMET"
