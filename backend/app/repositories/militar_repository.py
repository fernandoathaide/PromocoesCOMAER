"""
Repository da entidade Militar.
"""

from __future__ import annotations

from backend.app.repositories.base_repository import BaseRepository
from domain.entities.militar import Militar
from domain.value_objects.antiguidade import Antiguidade
from domain.value_objects.idade import Idade
from domain.value_objects.nome import Nome
from domain.value_objects.numero_ordem import NumeroOrdem
from domain.value_objects.posto import Posto
from domain.value_objects.quadro import Quadro
from domain.value_objects.tempo_servico import TempoServico


class MilitarRepository(BaseRepository):
    """
    Repository responsável pelo acesso aos militares
    armazenados na camada RAW.
    """

    SQL_BASE = """
        SELECT *
        FROM raw.t_pesfis_comgep_dw
    """

    def _to_entity(
        self,
        row,
    ) -> Militar:
        """
        Converte um registro do banco em uma Entity Militar.
        """

        return Militar(
            numero_ordem=NumeroOrdem(row["nr_ordem"]),
            nome=Nome(
                completo=row["nm_pessoa"],
                guerra=row["nm_guerra"],
            ),
            posto=Posto.from_codigo(
                row["sg_posto"],
            ),
            quadro=Quadro.from_codigo(
                row["sg_qdr"],
            ),
            antiguidade=Antiguidade(
                row["nr_antig"],
            ),
            idade=Idade(
                row["dt_nasc"],
            ),
            tempo_servico=TempoServico(
                row["tx_tempo_servico"],
            ),
            organizacao=row["sg_org"],
            data_praca=row["dt_praca"],
            data_promocao=row["dt_promocao_atual"],
            media_cfr=float(row["vl_med_cfr"] or 0),
            situacao_quadro=row["sg_sit_qdr"],
            numero_situacao=row["nr_sit_qdr"],
            movimentacao=row["st_mov"],
            veterano=row["st_veterano"] == "S",
            especial=row["st_especial"] == "S",
        )

    def listar(self) -> list[Militar]:
        """
        Retorna todos os militares.
        """

        rows = self.fetch_all(self.SQL_BASE)

        return [self._to_entity(row) for row in rows]

    def buscar_por_numero_ordem(
        self,
        numero_ordem: str,
    ) -> Militar | None:
        """
        Busca um militar pelo Número de Ordem.
        """

        row = self.fetch_one(
            self.SQL_BASE
            + """
            WHERE nr_ordem = :numero_ordem
            """,
            {
                "numero_ordem": numero_ordem,
            },
        )

        if row is None:
            return None

        return self._to_entity(row)

    def listar_por_posto(
        self,
        posto: str,
    ) -> list[Militar]:
        """
        Lista todos os militares de um posto.
        """

        rows = self.fetch_all(
            self.SQL_BASE
            + """
            WHERE sg_posto = :posto
            ORDER BY nr_antig
            """,
            {
                "posto": posto,
            },
        )

        return [self._to_entity(row) for row in rows]

    def quantidade(self) -> int:
        """
        Retorna a quantidade de militares.
        """

        total = self.scalar(
            """
            SELECT COUNT(*)
            FROM raw.t_pesfis_comgep_dw
            """
        )

        if total is None:
            return 0

        return int(total)
