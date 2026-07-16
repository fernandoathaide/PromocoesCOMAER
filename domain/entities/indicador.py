"""
Entity Indicador.

Representa os indicadores produzidos
por uma simulação.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Indicador:
    """
    Indicadores da simulação.
    """

    promocoes: int = 0

    reservas: int = 0

    vagas_abertas: int = 0

    vagas_ocupadas: int = 0

    militares_elegiveis: int = 0

    @property
    def saldo_vagas(self) -> int:
        """
        Saldo entre vagas abertas e ocupadas.
        """

        return self.vagas_abertas - self.vagas_ocupadas

    @property
    def houve_promocoes(self) -> bool:
        """
        Indica se houve promoções.
        """

        return self.promocoes > 0

    @property
    def quantidade_promocoes(self) -> int:
        return self.promocoes

    @property
    def quantidade_reservas(self) -> int:
        return self.reservas

    @property
    def quantidade_vagas_abertas(self) -> int:
        return self.vagas_abertas

    @property
    def quantidade_vagas_ocupadas(self) -> int:
        return self.vagas_ocupadas

    @property
    def quantidade_elegiveis(self) -> int:
        return self.militares_elegiveis

    def registrar_promocao(self) -> None:
        self.promocoes += 1

    def registrar_reserva(self) -> None:
        self.reservas += 1

    def abrir_vaga(self) -> None:
        self.vagas_abertas += 1

    def ocupar_vaga(self) -> None:
        self.vagas_ocupadas += 1

    def registrar_elegivel(self) -> None:
        self.militares_elegiveis += 1

    def __str__(self) -> str:
        return (
            "Indicadores("
            f"promoções={self.promocoes}, "
            f"reservas={self.reservas}, "
            f"vagas={self.vagas_abertas}/{self.vagas_ocupadas}, "
            f"elegíveis={self.militares_elegiveis}"
            ")"
        )

    def __repr__(self) -> str:
        return self.__str__()
