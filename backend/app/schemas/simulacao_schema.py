"""
Schemas da simulação.
"""

from pydantic import BaseModel

from backend.app.schemas.indicador_schema import IndicadorResponse
from backend.app.schemas.promocao_schema import PromocaoResponse


class SimulacaoResumoResponse(BaseModel):
    """
    Resumo da simulação.
    """

    militares: int

    promocoes: int

    reservas: int

    vagas: int

    elegiveis: int


class SimulacaoExecutadaResponse(BaseModel):
    """
    Resultado completo da execução da simulação.
    """

    indicadores: IndicadorResponse

    promocoes: list[PromocaoResponse]
