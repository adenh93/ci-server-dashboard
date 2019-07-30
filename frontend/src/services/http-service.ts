import axios from 'axios'
import { injectable, inject } from 'inversify';
import { IBrowserStorageService } from './browser-storage-service'
import { TYPES } from '@/ioc/types';
import { IAuthToken } from '@/typings/model';

export interface IHttpService {
    getTravis<T>(url: string, params?:any): Promise<T>;
    postTravis<T>(url: string, data: any): Promise<T>;
    getApi<T>(url: string, params?:any): Promise<T>;
    postApi<T>(url: string, data: any): Promise<T>;
}

@injectable()
export class HttpService implements IHttpService {

    apiBaseUrl: string = process.env.VUE_APP_API_BASE_URL;
    travisBaseUrl: string = process.env.VUE_APP_TRAVIS_BASE_URL;

    public constructor(
        @inject(TYPES.IBrowserStorageService) 
        private browserStorageService : IBrowserStorageService
    ) {
    }

    async getTravis<T>(url: string, params:any = null): Promise<T> {
        var token = this.browserStorageService.getTravisAuth();
        url = `${this.travisBaseUrl}/${url}`
        return await this.get<T>(url, token, params);
    }

    async postTravis<T>(url: string, data: any): Promise<T> {
        var token = this.browserStorageService.getTravisAuth();
        url = `${this.travisBaseUrl}/${url}`
        return await this.post<T>(url, token, data);
    }

    async getApi<T>(url: string, params:any = null): Promise<T> {
        var token = this.browserStorageService.getDashboardAuth();
        url = `${this.apiBaseUrl}/${url}`;
        return await this.get<T>(url, token, params);
    }

    async postApi<T>(url: string, data: any): Promise<T> {
        var token = this.browserStorageService.getDashboardAuth();
        url = `${this.apiBaseUrl}/${url}`;
        return await this.post<T>(url, token, data);
    }

    async get<T>(url: string, token: string, params:any = null): Promise<T> {
        var options = {
            headers: {'Authentication': `Bearer ${token}`},
            params: params
        }

        return await axios.get<T, T>(url, options)
            .catch((error) => {
                throw new Error(error);
            }
        )
    }

    async post<T>(url: string, token: string, data: any): Promise<T> {
        var options = {
            headers: {'Authentication': `Bearer ${token}`}
        }

        return await axios.post<any, T>(url, data)
            .catch((error) => {
                throw new Error(error);
            }
        )
    }
}