import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AcaoSimulacao } from './acao-simulacao';

describe('AcaoSimulacao', () => {
  let component: AcaoSimulacao;
  let fixture: ComponentFixture<AcaoSimulacao>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AcaoSimulacao],
    }).compileComponents();

    fixture = TestBed.createComponent(AcaoSimulacao);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
