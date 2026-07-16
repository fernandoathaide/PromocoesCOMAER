"""
Schemas relacionados às promoções.
"""

from pydantic import BaseModel


class PromocaoResponse(BaseModel):
    """
    Representa uma promoção realizada.
    """

    numero_ordem: str

    nome: str

    posto_origem: str

    posto_destino: str
