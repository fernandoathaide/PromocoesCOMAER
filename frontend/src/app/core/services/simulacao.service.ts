import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';

import { environment } from '../../../environments/environment';
import { Simulacao } from '../models/simulacao.model';

@Injectable({
  providedIn: 'root'
})
export class SimulacaoService {

  private readonly http = inject(HttpClient);

  private readonly api =
    `${environment.apiUrl}/simulacao`;

  getSimulacao(): Observable<Simulacao> {

    return this.http.get<Simulacao>(this.api);

  }

}
