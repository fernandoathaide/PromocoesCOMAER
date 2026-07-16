"""
Schemas dos indicadores.
"""

from pydantic import BaseModel


class IndicadorResponse(BaseModel):
    """
    Indicadores produzidos pela simulação.
    """

    promocoes: int

    reservas: int

    vagas_abertas: int

    vagas_ocupadas: int

    militares_elegiveis: int

    saldo_vagas: int
