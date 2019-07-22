<template>
    <div class="home mt-3">
        <b-row>
            <login-card></login-card>
        </b-row>
    </div>
</template>

<script lang="ts">
  import { Component, Vue } from "vue-property-decorator";
  import LoginCard from "@/components/login-card/LoginCard.vue";

  @Component({
    components: {
      LoginCard
    }
  })

  export default class Login extends Vue {

  }
</script>
