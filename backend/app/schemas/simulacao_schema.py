"""
Schemas da simulação.
"""

from pydantic import BaseModel


class SimulacaoResumoResponse(BaseModel):
    """
    Resumo da simulação.
    """

    militares: int

    promocoes: int

    reservas: int

    vagas: int

    elegiveis: int
