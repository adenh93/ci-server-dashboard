import { Container } from 'inversify';
import { IAuthService, AuthService } from '@/services/auth-service';
import { TYPES } from './types';
import { IBrowserStorageService, BrowserStorageService } from '@/services/browser-storage-service';
import { IBuildService, BuildService } from '@/services/build-service';
import { IHttpService, HttpService } from '@/services/http-service';
import getDecorators from 'inversify-inject-decorators';

const container = new Container();

container.bind<IAuthService>(TYPES.IAuthService).to(AuthService)
container.bind<IBrowserStorageService>(TYPES.IBrowserStorageService).to(BrowserStorageService)
container.bind<IBuildService>(TYPES.IBuildService).to(BuildService)
container.bind<IHttpService>(TYPES.IHttpService).to(HttpService)

const { lazyInject } = getDecorators(container);

export { container, lazyInject }