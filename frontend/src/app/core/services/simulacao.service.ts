import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';

import { API } from '../constants/api.constants';
import { ResultadoSimulacao } from '../models/resultado-simulacao.model';

@Injectable({
  providedIn: 'root',
})
export class SimulacaoService {
  private readonly http = inject(HttpClient);

  private readonly api = API.simulacao;

  getSimulacao(): Observable<ResultadoSimulacao> {
    return this.http.get<ResultadoSimulacao>(`${this.api}/`, {});
  }

  executarSimulacao(): Observable<ResultadoSimulacao> {
    return this.http.post<ResultadoSimulacao>(`${this.api}/executar`, {});
  }
}
