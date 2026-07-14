"""
Value Object - Quadro Militar.
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.enums.codigo_quadro import CodigoQuadro


@dataclass(frozen=True)
class Quadro:
    """
    Representa um Quadro do COMAER.
    """

    codigo: CodigoQuadro

    _QUADROS = {
        CodigoQuadro.QOAV: "QUADRO DE OFICIAIS AVIADORES",
        CodigoQuadro.QOINT: "QUADRO DE OFICIAIS INTENDENTES",
        CodigoQuadro.QOMED: "QUADRO DE OFICIAIS MÉDICOS",
        CodigoQuadro.QODENT: "QUADRO DE OFICIAIS DENTISTAS",
        CodigoQuadro.QOFARM: "QUADRO DE OFICIAIS FARMACÊUTICOS",
        CodigoQuadro.QOINF: "QUADRO DE OFICIAIS DE INFANTARIA",
        CodigoQuadro.QOENG: "QUADRO DE OFICIAIS ENGENHEIROS",
        CodigoQuadro.QOCAPL: "QUADRO DE OFICIAIS CAPELÃES",
        CodigoQuadro.QOEARM: "QUADRO DE OFICIAIS ESPECIALISTAS EM ARMAMENTO",
        CodigoQuadro.QOEAV: "QUADRO DE OFICIAIS ESPECIALISTAS EM AVIÕES",
        CodigoQuadro.QOECOM: "QUADRO DE OFICIAIS ESPECIALISTAS EM COMUNICAÇÕES",
        CodigoQuadro.QOECTA: ("QUADRO DE OFICIAIS ESPECIALISTAS EM CONTROLE DE TRÁFEGO AÉREO"),
        CodigoQuadro.QOEFOT: "QUADRO DE OFICIAIS ESPECIALISTAS EM FOTOGRAFIA",
        CodigoQuadro.QOEMET: "QUADRO DE OFICIAIS ESPECIALISTAS EM METEOROLOGIA",
    }

    @classmethod
    def from_codigo(
        cls,
        codigo: str,
    ) -> "Quadro":

        return cls(CodigoQuadro(codigo.upper().strip()))

    @property
    def descricao(self) -> str:

        return self._QUADROS[self.codigo]

    def __str__(self) -> str:

        return self.descricao

    def __repr__(self) -> str:

        return f"Quadro(codigo='{self.codigo.value}')"
