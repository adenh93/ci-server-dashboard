import { injectable } from 'inversify';
import { IAuthToken } from '@/typings/model';

export interface IBrowserStorageService {
    setTravisAuth(token: IAuthToken): void;
    getTravisAuth(): string;
    setDashboardAuth(token: IAuthToken): void;
    getDashboardAuth(): string;
}

@injectable()
export class BrowserStorageService implements IBrowserStorageService {
    
    setTravisAuth(token: IAuthToken): void {
        this.setItem('travis-auth', token);
    }

    getTravisAuth(): string {
        var auth = this.getItem<IAuthToken>('travis-auth');
        if (auth) return auth.access_token;
        return '';
    }

    setDashboardAuth(token: IAuthToken): void {
        this.setItem('dashboard-auth', token);
    }

    getDashboardAuth(): string {
        var auth = this.getItem<IAuthToken>('dashboard-auth');
        if (auth) return auth.access_token;
        return '';
    }

    setItem(key: string, data: any): void {
        var toStore = JSON.stringify(data);
        sessionStorage.setItem(key, toStore);
    }

    getItem<T>(key: string): T | null {
        var data = sessionStorage.getItem(key);
        if (!data) {
            return null;
        }
        return JSON.parse(data);
    }
}