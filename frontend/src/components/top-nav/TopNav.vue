<template>
    <b-navbar toggleable="lg" type="dark" class="app-nav">
      <b-navbar-brand href="#">CI Dashboard</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
          </b-navbar-nav>
        </b-collapse>
    </b-navbar>    
</template>

<script lang="ts">
  import { Component, Vue } from "vue-property-decorator";

  @Component
  export default class TopNav extends Vue {

  }
</script>

<style lang="scss" scoped>
  @import '../../main.scss';
  
</style>
