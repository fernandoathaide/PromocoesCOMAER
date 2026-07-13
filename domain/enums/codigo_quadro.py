"""
Enum dos Quadros do COMAER.
"""

from enum import Enum


class CodigoQuadro(str, Enum):
    QOAV = "QOAV"
    QOCAPL = "QOCAPL"
    QODENT = "QODENT"
    QOECOM = "QOECOM"
    QOEARM = "QOEARM"
    QOEAV = "QOEAV"
    QOECTA = "QOECTA"
    QOEFOT = "QOEFOT"
    QOEMET = "QOEMET"
    QOENG = "QOENG"
    QOFARM = "QOFARM"
    QOINF = "QOINF"
    QOINT = "QOINT"
    QOMED = "QOMED"

    @property
    def descricao(self):

        return {
            CodigoQuadro.QOAV: "Quadro de Oficiais Aviadores",
            CodigoQuadro.QOCAPL: "Quadro de Oficiais Capelães",
            CodigoQuadro.QODENT: "Quadro de Oficiais Dentistas",
            CodigoQuadro.QOECOM: "Quadro de Oficiais Especialistas em Comunicações",
            CodigoQuadro.QOEARM: "Quadro de Oficiais Especialistas em Armamento",
            CodigoQuadro.QOEAV: "Quadro de Oficiais Especialistas em Aviões",
            CodigoQuadro.QOECTA: "Quadro de Oficiais Especialistas em Controle de Tráfego Aéreo",
            CodigoQuadro.QOEFOT: "Quadro de Oficiais Especialistas em Fotografia",
            CodigoQuadro.QOEMET: "Quadro de Oficiais Especialistas em Meteorologia",
            CodigoQuadro.QOENG: "Quadro de Oficiais Engenheiros",
            CodigoQuadro.QOFARM: "Quadro de Oficiais Farmacêuticos",
            CodigoQuadro.QOINF: "Quadro de Oficiais de Infantaria",
            CodigoQuadro.QOINT: "Quadro de Oficiais Intendentes",
            CodigoQuadro.QOMED: "Quadro de Oficiais Médicos",
        }[self]
