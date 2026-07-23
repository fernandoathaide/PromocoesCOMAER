import { ChangeDetectionStrategy, Component, Input } from '@angular/core';

import { ResultadoSimulacao } from '../../../../core/models/resultado-simulacao.model';

import { StatCard } from '../../../../shared/components/stat-card/stat-card';

@Component({
  selector: 'app-painel-indicadores',
  standalone: true,
  imports: [StatCard],
  templateUrl: './painel-indicadores.html',
  styleUrl: './painel-indicadores.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class PainelIndicadores {
  @Input({ required: true })
  resultado!: ResultadoSimulacao;
}
