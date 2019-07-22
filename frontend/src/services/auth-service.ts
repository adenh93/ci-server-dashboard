import { IHttpService } from '@/services/http-service';
import { IBrowserStorageService } from '@/services/browser-storage-service';
import { inject, injectable } from 'inversify';
import { ILoginResponse } from '@/typings/model';
import { TYPES } from '@/ioc/types';

export interface IAuthService {
    login(formData: any): Promise<any>;
}

@injectable()
export class AuthService implements IAuthService {

    public constructor(
        @inject(TYPES.IHttpService)
        private httpService: IHttpService,
        @inject(TYPES.IBrowserStorageService)
        private browserStorageService: IBrowserStorageService
    ) {
    }

    async login(formData: any): Promise<void> {
        this.httpService.postApi<ILoginResponse>('auth/login', formData)
            .then((response) => {
                this.browserStorageService.setDashboardAuth(response.access_token);
                if(response.travis_token) {
                    this.browserStorageService.setTravisAuth(response.travis_token)
                }
            });
    }

}