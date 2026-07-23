import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaPromocoes } from './lista-promocoes';

describe('ListaPromocoes', () => {
  let component: ListaPromocoes;
  let fixture: ComponentFixture<ListaPromocoes>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListaPromocoes],
    }).compileComponents();

    fixture = TestBed.createComponent(ListaPromocoes);
    component = fixture.componentInstance;

    component.promocoes = [];

    fixture.detectChanges();

    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
