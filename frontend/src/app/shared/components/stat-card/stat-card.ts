import { Component, input } from '@angular/core';

import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-stat-card',
  standalone: true,
  imports: [
    MatCardModule,
    MatIconModule
  ],
  templateUrl: './stat-card.html',
  styleUrl: './stat-card.scss'
})
export class StatCard {

  readonly titulo = input.required<string>();

  readonly valor = input.required<number>();

  readonly icone = input.required<string>();

}
