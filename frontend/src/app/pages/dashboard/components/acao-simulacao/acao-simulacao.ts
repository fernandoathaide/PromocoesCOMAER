import { ChangeDetectionStrategy, Component, EventEmitter, Input, Output } from '@angular/core';

import { MatButtonModule } from '@angular/material/button';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

@Component({
  selector: 'app-acao-simulacao',
  standalone: true,
  imports: [MatButtonModule, MatProgressSpinnerModule],
  templateUrl: './acao-simulacao.html',
  styleUrl: './acao-simulacao.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class AcaoSimulacao {
  @Input()
  carregando = false;

  @Output()
  executar = new EventEmitter<void>();

  executarSimulacao(): void {
    this.executar.emit();
  }
}
