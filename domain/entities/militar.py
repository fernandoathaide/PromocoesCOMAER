"""
Entity Militar.

Representa um Oficial-General do COMAER dentro do domínio
do PromocoesCOMAER.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from domain.value_objects.antiguidade import Antiguidade
from domain.value_objects.idade import Idade
from domain.value_objects.nome import Nome
from domain.value_objects.numero_ordem import NumeroOrdem
from domain.value_objects.posto import Posto
from domain.value_objects.quadro import Quadro
from domain.value_objects.tempo_servico import TempoServico


@dataclass
class Militar:
    """
    Entidade principal do domínio.
    """

    numero_ordem: NumeroOrdem

    nome: Nome

    posto: Posto

    quadro: Quadro

    antiguidade: Antiguidade

    idade: Idade

    tempo_servico: TempoServico

    organizacao: str

    data_praca: date

    data_promocao: date

    media_cfr: float | None = None

    veterano: bool = False

    especial: bool = False

    movimentado: bool = False
