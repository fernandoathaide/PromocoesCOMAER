import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  OnInit,
  inject,
} from '@angular/core';

import { ResultadoSimulacao } from '../../core/models/resultado-simulacao.model';
import { SimulacaoService } from '../../core/services/simulacao.service';

import { PainelIndicadores } from './components/painel-indicadores/painel-indicadores';
import { ListaPromocoes } from './components/lista-promocoes/lista-promocoes';
import { AcaoSimulacao } from './components/acao-simulacao/acao-simulacao';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [PainelIndicadores, ListaPromocoes, AcaoSimulacao],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.scss',
  changeDetection: ChangeDetectionStrategy.Default,
})
export class Dashboard implements OnInit {
  private readonly simulacaoService = inject(SimulacaoService);
  private readonly cdr = inject(ChangeDetectorRef);

  resultado?: ResultadoSimulacao;
  carregando = false;

  ngOnInit(): void {
    this.simulacaoService.getSimulacao().subscribe({
      next: (dados) => {
        this.resultado = dados;

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

  executarSimulacao(): void {
    this.carregando = true;

    this.simulacaoService.executarSimulacao().subscribe({
      next: (dados) => {
        this.resultado = dados;

        this.carregando = false;

        this.cdr.markForCheck();
      },

      error: (erro) => {
        this.carregando = false;

        console.error(erro);

        this.cdr.markForCheck();
      },
    });
  }
}
