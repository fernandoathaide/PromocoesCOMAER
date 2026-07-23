import { AfterViewInit, ChangeDetectionStrategy, Component, Input, ViewChild } from '@angular/core';

import { MatCardModule } from '@angular/material/card';
import { MatSort, MatSortModule } from '@angular/material/sort';
import { MatTableDataSource, MatTableModule } from '@angular/material/table';

import { Promocao } from '../../../../core/models/promocao.model';

@Component({
  selector: 'app-lista-promocoes',
  standalone: true,
  imports: [MatCardModule, MatTableModule, MatSortModule],
  templateUrl: './lista-promocoes.html',
  styleUrl: './lista-promocoes.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ListaPromocoes implements AfterViewInit {
  @ViewChild(MatSort)
  sort!: MatSort;

  private readonly dataSource = new MatTableDataSource<Promocao>();

  @Input({ required: true })
  set promocoes(value: Promocao[]) {
    this.dataSource.data = value;
  }

  get promocoes(): Promocao[] {
    return this.dataSource.data;
  }

  readonly displayedColumns = ['numero_ordem', 'nome', 'posto_origem', 'posto_destino'];

  ngAfterViewInit(): void {
    this.dataSource.sort = this.sort;
  }

  get tabela(): MatTableDataSource<Promocao> {
    return this.dataSource;
  }
}
