import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GraficoIndicadores } from './grafico-indicadores';

describe('GraficoIndicadores', () => {
  let component: GraficoIndicadores;
  let fixture: ComponentFixture<GraficoIndicadores>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GraficoIndicadores],
    }).compileComponents();

    fixture = TestBed.createComponent(GraficoIndicadores);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
