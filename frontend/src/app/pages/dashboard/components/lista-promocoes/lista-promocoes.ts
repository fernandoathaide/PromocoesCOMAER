import { ChangeDetectionStrategy, Component, Input } from '@angular/core';

import { MatCardModule } from '@angular/material/card';
import { MatTableModule } from '@angular/material/table';

import { Promocao } from '../../../../core/models/promocao.model';

@Component({
  selector: 'app-lista-promocoes',
  standalone: true,
  imports: [MatCardModule, MatTableModule],
  templateUrl: './lista-promocoes.html',
  styleUrl: './lista-promocoes.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ListaPromocoes {
  @Input({ required: true })
  promocoes!: Promocao[];

  readonly displayedColumns = ['numero_ordem', 'nome', 'posto_origem', 'posto_destino'];
}
