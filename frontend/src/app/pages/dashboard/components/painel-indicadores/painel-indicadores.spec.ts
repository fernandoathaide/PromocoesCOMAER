import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PainelIndicadores } from './painel-indicadores';

describe('PainelIndicadores', () => {
  let component: PainelIndicadores;
  let fixture: ComponentFixture<PainelIndicadores>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PainelIndicadores],
    }).compileComponents();

    fixture = TestBed.createComponent(PainelIndicadores);

    component = fixture.componentInstance;

    component.resultado = {
      indicadores: {
        promocoes: 2,
        reservas: 0,
        vagas_abertas: 2,
        vagas_ocupadas: 0,
        militares_elegiveis: 0,
        saldo_vagas: 2,
      },
      promocoes: [],
    };

    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
