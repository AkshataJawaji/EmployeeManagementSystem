import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';
import { provideHttpClient, withFetch } from '@angular/common/http';
import { LoginComponent } from './app/login/login.component';

bootstrapApplication(AppComponent,appConfig)
  .catch((err) => console.error(err));

//   bootstrapApplication(LoginComponent, {
//     providers: [provideHttpClient()], // Use provideHttpClient here
//   }).catch;

  // bootstrapApplication(AppComponent, {
  //   ...appConfig,
  //   providers: [provideHttpClient(withFetch())], // Include HttpClient provider here
  // }).catch((err) => console.error(err));