import { ChangeDetectorRef, Component, OnInit, inject } from '@angular/core';

import { Simulacao } from '../../core/models/simulacao.model';
import { SimulacaoService } from '../../core/services/simulacao.service';

import { StatCard } from '../../shared/components/stat-card/stat-card';
import { JsonPipe } from '@angular/common';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [StatCard, JsonPipe],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.scss',
})
export class Dashboard implements OnInit {
  private readonly simulacaoService = inject(SimulacaoService);
  private readonly cdr = inject(ChangeDetectorRef);

  simulacao?: Simulacao;

  ngOnInit(): void {
    this.simulacaoService.getSimulacao().subscribe({
      next: dados => {

        console.log('Dashboard:', dados);

        this.simulacao = dados;

        this.cdr.detectChanges();

      },

      error: (erro) => {
        console.error('Erro ao consultar API', erro);
      },
    });
  }
}
