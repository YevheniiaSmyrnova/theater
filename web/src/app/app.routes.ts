import { Routes, RouterModule, RouterLinkActive }     from '@angular/router';
import { ModuleWithProviders }                        from '@angular/core';

import { AppComponent }                               from './app.component';


export const appRoutes: Routes =[
    { path: '',                           component: AppComponent }
];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);
