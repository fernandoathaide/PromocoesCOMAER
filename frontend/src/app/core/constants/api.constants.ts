import { environment } from '../../../environments/environment';

export const API = {

  simulacao: `${environment.apiUrl}/simulacao/`,

  executarSimulacao: `${environment.apiUrl}/simulacao/executar/`,

  militares: `${environment.apiUrl}/militares/`,

  promocoes: `${environment.apiUrl}/promocoes/`,

  reservas: `${environment.apiUrl}/reservas/`,

  vagas: `${environment.apiUrl}/vagas/`

};
