import { TestBed } from '@angular/core/testing';

import { Promocao } from './promocao';

describe('Promocao', () => {
  let service: Promocao;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Promocao);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
