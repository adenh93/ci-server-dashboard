<template>
  <b-nav vertical class="app-nav sidebar col-md-1">
      <b-nav-text class="pl-3">Servers</b-nav-text>
      <b-nav-item class="pl-4" active>
      <i class="icon-travis-ci ci-logo"/>
          Travis CI
      </b-nav-item>
  </b-nav>
</template>

<script lang="ts">
  import { Component, Vue } from "vue-property-decorator";

  @Component
  export default class SideNav extends Vue {

  }
</script>

<style lang="scss" scoped>
  @import '../../main.scss';

  .ci-logo {
    font-size: 2.1em;
  }
</style>