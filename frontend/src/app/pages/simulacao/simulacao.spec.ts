import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Simulacao } from './simulacao';

describe('Simulacao', () => {
  let component: Simulacao;
  let fixture: ComponentFixture<Simulacao>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Simulacao],
    }).compileComponents();

    fixture = TestBed.createComponent(Simulacao);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
