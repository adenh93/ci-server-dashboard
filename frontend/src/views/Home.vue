<template>
  <div class="home mt-3">
    <b-row>
      <b-col cols="12">
        <b-input-group>
          <b-form-input placeholder="Filter..." class="col-md-12" />
          <b-input-group-append>
            <b-button variant="default"><i class="icon-search"/> Search</b-button>
          </b-input-group-append>
        </b-input-group>
      </b-col>
    </b-row>
    <b-row>
      <b-col cols="12" class="mt-2">
        <b-card-group columns>
          <span v-for="n in 12">
            <build-card :build="build"/>
          </span>
        </b-card-group>
      </b-col>
    </b-row>
  </div>
</template>

<script lang="ts">
  import { Component, Vue } from "vue-property-decorator";
  import BuildCard from "@/components/build-card/BuildCard.vue";
  import { Build, BuildArtifact } from "@/typings/model";

  @Component({
    components: {
      BuildCard
    }
  })

  export default class Home extends Vue {
    
    private build: Build = {
      slug: "adenh93/typemallow",
      build_status: "passed",
      build_completed_time: new Date(),
      build_duration: 15,
      build_artifacts: [
        {
          file_name: "dist/typemallow-0.0.4.tar.gz",
          file_size: 13
        }
      ],
      commit_branch: "master",
      commit_hash: "0a4563f",
      commit_message: "Bumped version to 0.0.4",
      commit_author: "adenh93",
      commit_author_thumb_url: ""
    };

  }
</script>
