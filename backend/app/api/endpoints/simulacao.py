"""
Endpoints da simulação.
"""

from fastapi import APIRouter

from backend.app.schemas.indicador_schema import IndicadorResponse
from backend.app.schemas.promocao_schema import PromocaoResponse
from backend.app.schemas.resultado_simulacao_schema import (
    ResultadoSimulacaoResponse,
)
from backend.app.services.motor_simulacao import MotorSimulacao

router = APIRouter()


def montar_resultado(
    motor: MotorSimulacao,
) -> ResultadoSimulacaoResponse:
    """
    Converte o estado atual da simulação para o DTO de resposta.
    """

    promocoes = [
        PromocaoResponse(
            numero_ordem=p.militar.numero_ordem.valor,
            nome=p.militar.nome_guerra,
            posto_origem=p.posto_origem.nome,
            posto_destino=p.posto_destino.nome,
        )
        for p in motor.simulacao.promocoes
    ]

    return ResultadoSimulacaoResponse(
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


@router.get(
    "/",
    response_model=ResultadoSimulacaoResponse,
)
def resumo():
    """
    Retorna o estado atual da simulação.
    """

    motor = MotorSimulacao()

    motor.carregar()

    resposta = montar_resultado(motor)

    motor.fechar()

    return resposta


@router.post(
    "/executar",
    response_model=ResultadoSimulacaoResponse,
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

    resposta = montar_resultado(motor)

    motor.fechar()

    return resposta
