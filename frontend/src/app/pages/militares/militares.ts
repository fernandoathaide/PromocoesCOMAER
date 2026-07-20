import { Component, OnInit, AfterViewInit, ViewChild, inject } from '@angular/core';
import { MatTableDataSource, MatTableModule } from '@angular/material/table';
import { MatPaginator, MatPaginatorModule } from '@angular/material/paginator';
import { MatSort, MatSortModule } from '@angular/material/sort';

import { Militar } from '../../core/models/militar.model';
import { MilitarService } from '../../core/services/militar.service';

import { FormsModule } from '@angular/forms';

import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatCardModule } from '@angular/material/card';

@Component({
  selector: 'app-militares',
  standalone: true,
  imports: [
    FormsModule,

    MatCardModule,
    MatInputModule,
    MatFormFieldModule,

    MatTableModule,
    MatPaginatorModule,
    MatSortModule
  ],
  templateUrl: './militares.html',
  styleUrl: './militares.scss'
})
export class Militares implements OnInit, AfterViewInit {

  private readonly militarService = inject(MilitarService);
  filtro = '';

  displayedColumns: string[] = [
    'numero_ordem',
    'nome',
    'posto',
    'quadro'
  ];

  dataSource = new MatTableDataSource<Militar>();

  @ViewChild(MatPaginator)
  paginator!: MatPaginator;

  @ViewChild(MatSort)
  sort!: MatSort;

  ngOnInit(): void {

    this.militarService.listar().subscribe({

      // next: militares => {
      //   this.dataSource.data = militares;
      //   this.dataSource.filterPredicate = (data, filtro) => {
      //     const texto = (
      //       data.numero_ordem +
      //       data.nome +
      //       data.posto +
      //       data.quadro
      //     ).toLowerCase();

      //     return texto.includes(filtro);

      //   };
      // },

      next: militares => {

        console.log('Militares recebidos:', militares);
        console.log('Quantidade:', militares.length);

        this.dataSource.data = militares;

        this.dataSource.filterPredicate = (data, filtro) => {

          const texto = (
            data.numero_ordem +
            data.nome +
            data.posto +
            data.quadro
          ).toLowerCase();

          return texto.includes(filtro);

        };

      },

      error: erro => {
        console.error(erro);
      }

    });

  }

  ngAfterViewInit(): void {

    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;

  }

  aplicarFiltro(): void {

    this.dataSource.filter =
    this.filtro.trim().toLowerCase();

  }

}
