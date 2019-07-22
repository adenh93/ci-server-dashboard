<template>
  <div id="app">
    <top-nav></top-nav>
    <b-container fluid>
      <main role="main">
        <router-view />
      </main>
    </b-container>
  </div>
</template>

<script lang="ts">
  import { Component, Vue } from "vue-property-decorator";
  import TopNav from "@/components/top-nav/TopNav.vue";

  @Component({
    components: {
      TopNav
    }
  })

  export default class App extends Vue {

  }
</script>