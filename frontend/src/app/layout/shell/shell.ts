import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import { MatSidenavModule } from '@angular/material/sidenav';

import { Header } from '../header/header';
import { Sidebar } from '../sidebar/sidebar';
import { Footer } from '../footer/footer';

@Component({
  selector: 'app-shell',
  standalone: true,
  imports: [
    Header,
    Sidebar,
    Footer,
    RouterOutlet,
    MatSidenavModule
  ],
  templateUrl: './shell.html',
  styleUrl: './shell.scss'
})
export class Shell {}
