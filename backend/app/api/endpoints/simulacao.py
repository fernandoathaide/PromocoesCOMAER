"""
Endpoints da simulação.
"""

from fastapi import APIRouter

from backend.app.schemas.indicador_schema import IndicadorResponse
from backend.app.schemas.promocao_schema import PromocaoResponse
from backend.app.schemas.simulacao_schema import (
    SimulacaoExecutadaResponse,
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


@router.post(
    "/executar",
    response_model=SimulacaoExecutadaResponse,
)
def executar():
    """
    Executa uma simulação completa.
    """

    motor = MotorSimulacao()

    motor.carregar()

    #
    # Execução inicial apenas para validar
    # o pipeline da API.
    #
    motor.promover_mais_antigo(
        "BR",
        "QOAV",
    )

    promocoes = [
        PromocaoResponse(
            numero_ordem=p.militar.numero_ordem.valor,
            nome=p.militar.nome_guerra,
            posto_origem=p.posto_origem.nome,
            posto_destino=p.posto_destino.nome,
        )
        for p in motor.simulacao.promocoes
    ]

    resposta = SimulacaoExecutadaResponse(
        indicadores=IndicadorResponse(
            promocoes=motor.indicadores.promocoes,
            reservas=motor.indicadores.reservas,
            vagas_abertas=motor.indicadores.vagas_abertas,
            vagas_ocupadas=motor.indicadores.vagas_ocupadas,
            militares_elegiveis=motor.indicadores.militares_elegiveis,
            saldo_vagas=motor.indicadores.saldo_vagas,
        ),
        promocoes=promocoes,
    )

    motor.fechar()

    return resposta
