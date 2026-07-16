"""
Endpoints dos militares.
"""

from fastapi import APIRouter

from backend.app.services.militar_service import MilitarService

router = APIRouter()


@router.get("/")
def listar():

    service = MilitarService()

    militares = service.listar()

    service.fechar()

    return [
        {
            "numero_ordem": militar.numero_ordem.valor,
            "nome": militar.nome_guerra,
            "posto": militar.posto.nome,
            "quadro": militar.quadro.codigo.value,
        }
        for militar in militares
    ]
