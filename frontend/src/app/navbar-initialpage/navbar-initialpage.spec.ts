import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NavbarInitialpage } from './navbar-initialpage';

describe('NavbarInitialpage', () => {
  let component: NavbarInitialpage;
  let fixture: ComponentFixture<NavbarInitialpage>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NavbarInitialpage]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NavbarInitialpage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
