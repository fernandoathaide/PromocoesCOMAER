import { Component, OnInit, inject } from '@angular/core';

import { Simulacao } from '../../core/models/simulacao.model';
import { SimulacaoService } from '../../core/services/simulacao.service';

import { StatCard } from '../../shared/components/stat-card/stat-card';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    StatCard
  ],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.scss'
})
export class Dashboard implements OnInit {

  private readonly simulacaoService = inject(SimulacaoService);

  simulacao?: Simulacao;

  ngOnInit(): void {

    this.simulacaoService
      .getSimulacao()
      .subscribe({

        next: dados => {
          this.simulacao = dados;
        },

        error: erro => {
          console.error('Erro ao consultar API', erro);
        }

      });

  }

}
