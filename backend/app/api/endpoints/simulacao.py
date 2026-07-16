"""
Endpoints da simulação.
"""

from fastapi import APIRouter

from backend.app.schemas.simulacao_schema import (
    SimulacaoResumoResponse,
)
from backend.app.services.motor_simulacao import MotorSimulacao

router = APIRouter()


@router.get(
    "/",
    response_model=SimulacaoResumoResponse,
)
def resumo():

    motor = MotorSimulacao()

    simulacao = motor.carregar()

    resposta = SimulacaoResumoResponse(
        militares=simulacao.quantidade_militares,
        promocoes=simulacao.quantidade_promocoes,
        reservas=simulacao.quantidade_reservas,
        vagas=simulacao.quantidade_vagas,
        elegiveis=motor.indicadores.militares_elegiveis,
    )

    motor.fechar()

    return resposta
