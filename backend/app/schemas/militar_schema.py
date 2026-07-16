"""
Schemas relacionados aos militares.
"""

from pydantic import BaseModel


class MilitarResponse(BaseModel):
    """
    Resposta da API para militares.
    """

    numero_ordem: str

    nome: str

    posto: str

    quadro: str
