"""
Endpoints dos militares.
"""

from fastapi import APIRouter

from backend.app.schemas.militar_schema import MilitarResponse
from backend.app.services.militar_service import MilitarService

router = APIRouter()


@router.get(
    "/",
    response_model=list[MilitarResponse],
)
def listar():

    service = MilitarService()

    militares = service.listar()

    service.fechar()

    return [
        MilitarResponse(
            numero_ordem=militar.numero_ordem.valor,
            nome=militar.nome_guerra,
            posto=militar.posto.nome,
            quadro=militar.quadro.codigo.value,
        )
        for militar in militares
    ]
