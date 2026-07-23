import {
  ChangeDetectionStrategy,
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

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    PainelIndicadores,
    ListaPromocoes,
    AcaoSimulacao,
  ],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.scss',
  changeDetection: ChangeDetectionStrategy.Default,
})
export class Dashboard implements OnInit {
  private readonly simulacaoService = inject(SimulacaoService);
  private readonly destroyRef = inject(DestroyRef);

  resultado?: ResultadoSimulacao;

  carregando = false;

  ngOnInit(): void {
    this.simulacaoService
      .getSimulacao()
      .pipe(
        takeUntilDestroyed(this.destroyRef),
      )
      .subscribe({
        next: (dados) => {
          this.resultado = dados;
        },

        error: (erro) => {
          console.error(
            'Erro ao carregar indicadores do dashboard:',
            erro,
          );
        },
      });
  }

  executarSimulacao(): void {
    this.carregando = true;

    this.simulacaoService
      .executarSimulacao()
      .pipe(
        takeUntilDestroyed(this.destroyRef),
      )
      .subscribe({
        next: (dados) => {
          this.resultado = dados;
          this.carregando = false;
        },

        error: (erro) => {
          this.carregando = false;
          console.error(erro);
        },
      });
  }
}
