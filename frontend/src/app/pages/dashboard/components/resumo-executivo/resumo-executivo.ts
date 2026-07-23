import { ChangeDetectionStrategy, Component, computed, input } from '@angular/core';

import { MatCardModule } from '@angular/material/card';

import { ResultadoSimulacao } from '../../../../core/models/resultado-simulacao.model';

@Component({
  selector: 'app-resumo-executivo',
  standalone: true,
  imports: [MatCardModule],
  templateUrl: './resumo-executivo.html',
  styleUrl: './resumo-executivo.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ResumoExecutivo {
  readonly resultado = input.required<ResultadoSimulacao>();

  readonly resumo = computed(() => {
    const i = this.resultado().indicadores;

    return (
      `Foram encontradas ${i.promocoes} promoções, ` +
      `${i.reservas} reservas, ` +
      `${i.vagas_abertas} vagas abertas e ` +
      `${i.saldo_vagas} vagas disponíveis para movimentação.`
    );
  });
}
