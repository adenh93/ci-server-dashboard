<template>
    <b-card>
        <b-card-body>
            <b-card-title>Login</b-card-title>
            <b-card-text>
                <b-form>
                    <b-form-group label="Username:">
                        <b-form-input v-model="loginRequest.username" type="text" placeholder="Enter username..." required/>
                    </b-form-group>
                    <b-form-group label="Password:">
                        <b-form-input v-model="loginRequest.password" type="password" placeholder="Enter password..." required/>
                    </b-form-group>
                    <b-button variant="primary" role="button" v-on:click="login()">Submit</b-button>
                </b-form>
            </b-card-text>
        </b-card-body>
        <b-card-footer class="font-italic">
            <p>Don't have an account? <a href="#">Register</a>.</p>
        </b-card-footer>
    </b-card>
</template>

<script lang="ts">
  import { Component, Vue, Prop } from "vue-property-decorator";
  import { IAuthService } from "../../services/auth-service";
  import { INotificationService } from "../../services/notification-service";
  import { lazyInject } from '../../ioc/container';
  import { TYPES } from '../../ioc/types';
  import { ILoginRequest } from '../../typings/model';
  import router from "../../router";

  @Component
  export default class LoginCard extends Vue {
    @lazyInject(TYPES.IAuthService) private authService: IAuthService;
    @lazyInject(TYPES.INotificationService) private notificationService: INotificationService;
    @Prop() loginRequest: ILoginRequest = {}; 

    login() {
        this.authService.login(this.loginRequest)
            .then((request) => {
                router.push({ name: 'home' })
                this.notificationService.success(this, "Successfully logged in");
            }).catch((error: Error) => {
                this.notificationService.error(this, error.message);
            });
    }
  }
</script>

<style lang="scss" scoped>
  @import '../../main.scss';

  .card {
      border-radius: 0;
  }
  
  .card, .card-header, .card-footer {
    background-color: $theme-foreground;
  }
  
</style>
