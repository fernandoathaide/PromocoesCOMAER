import { Component, OnInit, AfterViewInit, ViewChild, inject } from '@angular/core';
import { MatTableDataSource, MatTableModule } from '@angular/material/table';
import { MatPaginator, MatPaginatorModule } from '@angular/material/paginator';
import { MatSort, MatSortModule } from '@angular/material/sort';

import { Militar } from '../../core/models/militar.model';
import { MilitarService } from '../../core/services/militar.service';

@Component({
  selector: 'app-militares',
  standalone: true,
  imports: [
    MatTableModule,
    MatPaginatorModule,
    MatSortModule
  ],
  templateUrl: './militares.html',
  styleUrl: './militares.scss'
})
export class Militares implements OnInit, AfterViewInit {

  private readonly militarService = inject(MilitarService);

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

      next: militares => {
        this.dataSource.data = militares;
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

}
