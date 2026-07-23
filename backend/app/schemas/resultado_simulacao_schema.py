"""
Schema do resultado da simulação.
"""

from pydantic import BaseModel

from .indicador_schema import IndicadorResponse
from .promocao_schema import PromocaoResponse


class ResultadoSimulacaoResponse(BaseModel):
    """
    Resultado completo produzido pela simulação.
    """

    indicadores: IndicadorResponse

    promocoes: list[PromocaoResponse]
