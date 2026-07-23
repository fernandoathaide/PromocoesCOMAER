import { TestBed } from '@angular/core/testing';

import { ResumoExecutivo } from './resumo-executivo';

describe('ResumoExecutivo', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ResumoExecutivo],
    }).compileComponents();
  });

  it('should create', () => {
    const fixture = TestBed.createComponent(ResumoExecutivo);

    fixture.componentRef.setInput('resultado', {
      indicadores: {
        promocoes: 2,
        reservas: 0,
        vagas_abertas: 2,
        vagas_ocupadas: 0,
        militares_elegiveis: 0,
        saldo_vagas: 2,
      },
      promocoes: [],
    });

    fixture.detectChanges();

    expect(fixture.componentInstance).toBeTruthy();
  });
});
