import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';

import { environment } from '../../../environments/environment';

import { Militar } from '../models/militar.model';

import { API } from '../constants/api.constants';

@Injectable({
  providedIn: 'root',
})
export class MilitarService {
  private readonly http = inject(HttpClient);

  private readonly api = API.militares;

  listar(): Observable<Militar[]> {
    return this.http.get<Militar[]>(`${this.api}/`, {});
  }
}
