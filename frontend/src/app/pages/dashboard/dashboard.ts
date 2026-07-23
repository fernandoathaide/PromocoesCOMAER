import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  DestroyRef,
  OnInit,
  inject,
} from '@angular/core';

import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

import { ResultadoSimulacao } from '../../core/models/resultado-simulacao.model';
import { SimulacaoService } from '../../core/services/simulacao.service';

import { AcaoSimulacao } from './components/acao-simulacao/acao-simulacao';
import { ListaPromocoes } from './components/lista-promocoes/lista-promocoes';
import { PainelIndicadores } from './components/painel-indicadores/painel-indicadores';
import { GraficoIndicadores } from './components/grafico-indicadores/grafico-indicadores';
import { ResumoExecutivo } from './components/resumo-executivo/resumo-executivo';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [PainelIndicadores, GraficoIndicadores, ListaPromocoes, AcaoSimulacao, ResumoExecutivo],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.scss',
  changeDetection: ChangeDetectionStrategy.Default,
})
export class Dashboard implements OnInit {
  private readonly simulacaoService = inject(SimulacaoService);
  private readonly destroyRef = inject(DestroyRef);
  private readonly cdr = inject(ChangeDetectorRef);

  resultado?: ResultadoSimulacao;

  carregando = false;

  ngOnInit(): void {
    this.simulacaoService
      .getSimulacao()
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe({
        next: (dados) => {
          this.resultado = dados;
          this.carregando = false;
          this.atualizarView();
        },

        error: (erro) => {
          console.error('Erro ao carregar indicadores do dashboard:', erro);
        },
      });
  }

  executarSimulacao(): void {
    this.carregando = true;

    this.simulacaoService
      .executarSimulacao()
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe({
        next: (dados) => {
          this.resultado = dados;
          this.carregando = false;
          this.atualizarView();
        },

        error: (erro) => {
          this.carregando = false;
          console.error(erro);
        },
      });
  }

  private atualizarView(): void {
    // Angular 22 + Vite:
    // Em alguns cenários a view não é atualizada automaticamente
    // após o retorno do HttpClient. Força a sincronização da UI.
    // Reavaliar após atualização do Angular.
    this.cdr.markForCheck();
  }
}
