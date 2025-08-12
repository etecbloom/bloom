import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavbarInitialpage } from "./navbar-initialpage/navbar-initialpage";

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, NavbarInitialpage],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('frontend');
}
