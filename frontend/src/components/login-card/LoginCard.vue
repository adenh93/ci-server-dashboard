<template>
    <b-card>
        <b-card-body>
            <b-card-title>Login</b-card-title>
            <b-card-text>
                <b-form>
                    <b-form-group label="Email Address:">
                        <b-form-input name="username" type="email" required placeholder="Enter email..."/>
                    </b-form-group>
                    <b-form-group label="Display Name:">
                        <b-form-input name="name" type="text" required placeholder="Enter display name..."/>
                    </b-form-group>
                    <b-form-group label="Password:">
                        <b-form-input name="password" type="password" required placeholder="Enter password..."/>
                    </b-form-group>
                    <b-button variant="primary" type="submit" v-on:click="login()">Submit</b-button>
                </b-form>
            </b-card-text>
        </b-card-body>
        <b-card-footer class="font-italic">
            <p>Don't have an account? <a href="#">Register</a>.</p>
        </b-card-footer>
    </b-card>
</template>

<script lang="ts">
  import { Component, Vue } from "vue-property-decorator";
  import { IAuthService } from "@/services/auth-service";
  import { lazyInject } from '@/ioc/container'
  import { TYPES } from '@/ioc/types'

  @Component
  export default class LoginCard extends Vue {
    @lazyInject(TYPES.IAuthService)
    authService: IAuthService;

    login(formData: any) {
        //TODO
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
