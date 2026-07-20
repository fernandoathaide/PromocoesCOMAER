import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Militares } from './militares';

describe('Militares', () => {
  let component: Militares;
  let fixture: ComponentFixture<Militares>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Militares],
    }).compileComponents();

    fixture = TestBed.createComponent(Militares);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
