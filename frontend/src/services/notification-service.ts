import { injectable } from 'inversify';
import { Vue } from "vue-property-decorator";
import { BvVariant } from '@/typings/enum';

export interface INotificationService {
    success(component: Vue, message: string): void;
    error(component: Vue, message: string): void;
    warning(component: Vue, message: string): void;
    info(component: Vue, message: string): void;
    showNotification(component: Vue, variant: BvVariant, message: string): void;
}

@injectable()
export class NotificationService implements INotificationService {
    
    success(component: Vue, message: string): void {
        this.showNotification(component, BvVariant.Success, message);
    }

    error(component: Vue, message: string): void {
        this.showNotification(component, BvVariant.Danger, message);
    }

    warning(component: Vue, message: string): void {
        this.showNotification(component, BvVariant.Warning, message);
    }

    info(component: Vue, message: string): void {
        this.showNotification(component, BvVariant.Info, message);
    }

    showNotification(component: Vue, variant: BvVariant, message: string): void {
        component.$bvToast.toast(message, {
            title: variant,
            variant: variant,
            autoHideDelay: 5000,
            appendToast: true
        });
    }
}