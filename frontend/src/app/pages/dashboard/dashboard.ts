import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  OnInit,
  inject,
} from '@angular/core';

import { Simulacao } from '../../core/models/simulacao.model';
import { SimulacaoService } from '../../core/services/simulacao.service';

import { StatCard } from '../../shared/components/stat-card/stat-card';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [StatCard],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.scss',
  changeDetection: ChangeDetectionStrategy.Default,
})
export class Dashboard implements OnInit {
  private readonly simulacaoService = inject(SimulacaoService);
  private readonly cdr = inject(ChangeDetectorRef);

  simulacao?: Simulacao;

  ngOnInit(): void {
    this.simulacaoService.getSimulacao().subscribe({
      next: (dados) => {
        this.simulacao = dados;

        // Workaround temporário para Angular 22 + Vite.
        // Sem esta chamada a view não é atualizada após o retorno do HttpClient.
        // Reavaliar após atualização do Angular.
        this.cdr.markForCheck();
      },

      error: (erro) => {
        console.error('Erro ao carregar indicadores do dashboard:', erro);
      },
    });
  }
}
