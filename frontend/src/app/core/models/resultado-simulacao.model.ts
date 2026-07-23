import { Indicadores } from './indicadores.model';
import { Promocao } from './promocao.model';

export interface ResultadoSimulacao {
  indicadores: Indicadores;

  promocoes: Promocao[];
}
