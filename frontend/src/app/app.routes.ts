import { Routes } from '@angular/router';

export const routes: Routes = [

  {
    path: '',
    redirectTo: 'dashboard',
    pathMatch: 'full'
  },

  {
    path: 'dashboard',
    loadComponent: () =>
      import('./pages/dashboard/dashboard')
        .then(c => c.Dashboard)
  },

  {
    path: 'militares',
    loadComponent: () =>
      import('./pages/militares/militares')
        .then(c => c.Militares)
  },

  {
      path: '**',
      redirectTo: 'dashboard'
  }

];
