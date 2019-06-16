<template>
  <div class="test">
    <b-card class="my-2">
      <b-card-header class="font-italic">
        <img src="../../assets/image/user-icon.png" height="30" width="30"/> {{build.commit_author}} - 12 days ago
        <span class="float-right"><fa-icon icon="clock"/> {{build.build_duration}} sec</span>
      </b-card-header>
      <b-card-body>
        <b-card-title>{{build.slug}}</b-card-title>
        <b-card-sub-title><i class="icon-flow-branch"/> {{build.commit_branch}}</b-card-sub-title>
        <b-card-text>
          <p class="font-italic"><small><i class="icon-github"/> {{build.commit_hash}} - {{build.commit_message}}</small></p>
        </b-card-text>
        <b-card-text>
          <h6 class="font-weight-bold">Build artifacts</h6>
          <b-list-group flush>
            <b-list-item v-for="artifact in build.build_artifacts">
              <a href="#"><i class="icon-download"/> {{artifact.file_name}} - {{artifact.file_size}}kb</a>
            </b-list-item>
          </b-list-group>
        </b-card-text>
      </b-card-body>
      <b-card-footer class="font-italic">
        <b-button variant="primary">
          <i class="icon-download"/> View build log
        </b-button>
      </b-card-footer>
    </b-card>
  </div>
</template>

<script lang="ts">
  import { Component, Prop, Vue } from "vue-property-decorator";
  import { Build, BuildArtifact } from "@/typings/model";

  @Component
  export default class BuildCard extends Vue {
    @Prop() private build: Build;
  }
</script>

<style lang="scss" scoped>
  @import '../../main.scss';

  .card {
      border-radius: 0;
      border-left: 3px solid rgba($theme-neon-green, 0.5);
  }

  .card, .card-header, .card-footer {
    background-color: $theme-foreground;
  }
  
</style>
