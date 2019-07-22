<template>
  <div>
    <b-row>
      <side-nav></side-nav>
      <div class="home mt-3 col-md-11">
        <build-list></build-list>
      </div>
    </b-row>
  </div>
</template>

<script lang="ts">
  import { Component, Vue } from "vue-property-decorator";
  import SideNav from "@/components/side-nav/SideNav.vue";
  import BuildList from "@/components/build-list/BuildList.vue";

  @Component({
    components: {
      SideNav,
      BuildList
    }
  })

  export default class Home extends Vue {

  }
</script>
