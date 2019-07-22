import { IHttpService } from '@/services/http-service';
import { IBuild } from '@/typings/model';
import { inject, injectable } from 'inversify';
import { TYPES } from '@/ioc/types';

export interface IBuildService {
    getBuilds(): Promise<IBuild[]>;
}

@injectable()
export class BuildService implements IBuildService {

    constructor(
        @inject(TYPES.IHttpService)
        private httpService: IHttpService
    ) {
    }

    async getBuilds(): Promise<IBuild[]> {
        return await this.httpService.getTravis<IBuild[]>('/builds')
            .then((response) => {
                return <IBuild[]>response;
            })        
    }
}