import { injectable } from 'inversify';
import { IAuthToken } from '@/typings/model';

export interface IBrowserStorageService {
    setTravisAuth(token: IAuthToken): void;
    getTravisAuth(): any;
    setDashboardAuth(token: IAuthToken): void;
    getDashboardAuth(): any;
}

@injectable()
export class BrowserStorageService implements IBrowserStorageService {
    
    setTravisAuth(token: IAuthToken): void {
        this.setItem('travis-auth', token);
    }

    getTravisAuth(): IAuthToken {
        return this.getItem<IAuthToken>('travis-auth');
    }

    setDashboardAuth(token: IAuthToken): void {
        this.setItem('dashboard-auth', token);
    }

    getDashboardAuth(): IAuthToken {
        return this.getItem<IAuthToken>('dashboard-auth');
    }

    setItem(key: string, data: any): void {
        var toStore = JSON.stringify(data);
        sessionStorage.setItem(key, toStore);
    }

    getItem<T>(key: string): T {
        var data = sessionStorage.getItem(key);
        if (!data) {
            throw new Error(`No item present for key: ${key}`)
        }
        return JSON.parse(data);
    }
}