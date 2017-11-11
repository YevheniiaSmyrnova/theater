import { NgModule }                                   from '@angular/core';
import { FormsModule }                                from '@angular/forms';
import { ReactiveFormsModule }                        from '@angular/forms';
import { FlexLayoutModule }                           from '@angular/flex-layout';
import { HttpModule, JsonpModule }                    from '@angular/http';
import { BrowserModule }                              from '@angular/platform-browser';
import { RouterModule }                               from '@angular/router';
import { NvD3Module }                                 from 'ng2-nvd3';
import { Select2Module }                              from 'ng2-select2';
import { ModalModule }                                from 'ngx-bootstrap';
import { ClipboardModule }                            from 'ngx-clipboard';
import { OrderModule }                                from 'ngx-order-pipe';
import 'd3';
import 'nvd3';
import { AppComponent }                               from './app.component';

import { appRoutes }                                  from './app.routes';

@NgModule({
    imports:         [ BrowserModule,
                       ClipboardModule,
                       FormsModule,
                       FlexLayoutModule,
                       HttpModule,
                       JsonpModule,
                       ModalModule.forRoot(),
                       NvD3Module,
                       OrderModule,
                       Select2Module,
                       ReactiveFormsModule,
                       RouterModule.forRoot(appRoutes) ],

    declarations:    [ AppComponent],

    bootstrap:       [ AppComponent ],
})
export class AppModule {}
