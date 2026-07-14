"""
Entity Militar.

Representa um Oficial do COMAER dentro do domínio da aplicação.
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

    media_cfr: float

    situacao_quadro: str | None = None

    numero_situacao: str | None = None

    movimentacao: str | None = None

    veterano: bool = False

    especial: bool = False

    @property
    def posto_atual(self) -> Posto:
        return self.posto

    @property
    def proximo_posto(self) -> Posto | None:
        return self.posto.proximo

    @property
    def nome_guerra(self) -> str:
        return self.nome.guerra

    @property
    def nome_completo(self) -> str:
        return self.nome.completo

    @property
    def anos_servico(self) -> int:
        return self.tempo_servico.anos

    @property
    def idade_anos(self) -> int:
        return self.idade.anos

    @property
    def eh_coronel(self) -> bool:
        return self.posto.eh_coronel

    @property
    def eh_brigadeiro(self) -> bool:
        return self.posto.eh_brigadeiro

    @property
    def eh_major_brigadeiro(self) -> bool:
        return self.posto.eh_major_brigadeiro

    @property
    def eh_tenente_brigadeiro(self) -> bool:
        return self.posto.eh_tenente_brigadeiro

    @property
    def eh_marechal(self) -> bool:
        return self.posto.eh_marechal

    def __str__(self) -> str:

        return f"{self.nome_guerra} ({self.posto})"

    def __repr__(self) -> str:

        return (
            "Militar("
            f"numero_ordem={self.numero_ordem}, "
            f"nome='{self.nome_guerra}', "
            f"posto='{self.posto}', "
            f"quadro='{self.quadro.codigo.value}'"
            ")"
        )
