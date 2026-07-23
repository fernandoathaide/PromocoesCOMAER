import { ChangeDetectionStrategy, Component, Input, OnChanges, SimpleChanges } from '@angular/core';
import { BaseChartDirective } from 'ng2-charts';
import { ChartConfiguration, ChartData } from 'chart.js';
import { ResultadoSimulacao } from '../../../../core/models/resultado-simulacao.model';
import { MatCardModule } from '@angular/material/card';

@Component({
  selector: 'app-grafico-indicadores',
  standalone: true,
  imports: [MatCardModule, BaseChartDirective],
  templateUrl: './grafico-indicadores.html',
  styleUrl: './grafico-indicadores.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class GraficoIndicadores implements OnChanges {
  @Input({ required: true })
  resultado!: ResultadoSimulacao;

  // Defina como o literal 'bar' exato para casar com ChartData<'bar'>
  readonly tipo: 'bar' = 'bar';

  dados: ChartData<'bar'> = {
    labels: [],
    datasets: [],
  };

  readonly opcoes: ChartConfiguration<'bar'>['options'] = {
    responsive: true,
    maintainAspectRatio: false,
  };

  ngOnChanges(changes: SimpleChanges): void {
    if (!changes['resultado'] || !this.resultado) {
      return;
    }

    const i = this.resultado.indicadores;

    // Criando uma nova referência para acionar a detecção OnPush
    this.dados = {
      labels: ['Promoções', 'Reservas', 'Vagas Abertas', 'Vagas Ocupadas', 'Elegíveis', 'Saldo'],
      datasets: [
        {
          label: 'Indicadores',
          data: [
            i.promocoes,
            i.reservas,
            i.vagas_abertas,
            i.vagas_ocupadas,
            i.militares_elegiveis,
            i.saldo_vagas,
          ],
        },
      ],
    };
  }
}
