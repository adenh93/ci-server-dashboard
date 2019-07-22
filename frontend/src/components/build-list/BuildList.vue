<template>
    <div>
        <b-row>
            <b-col cols="12">
                <b-input-group>
                <b-form-input placeholder="Filter..." class="col-md-12" />
                <b-input-group-append>
                    <b-button variant="default">
                        <i class="icon-search"/> Search
                    </b-button>
                </b-input-group-append>
                </b-input-group>
            </b-col>
        </b-row>
        <b-row>
            <b-col cols="12" class="mt-2">
                <b-card-group columns>
                    <span v-for="build in builds">
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
  import { IBuild, BuildArtifact } from "@/typings/model";
  import { IBuildService } from "@/services/build-service";
  import { lazyInject } from '@/ioc/container'
  import { TYPES } from '@/ioc/types'
  
  @Component({
    components: {
      BuildCard
    }
  })

  export default class BuildList extends Vue {

      private builds : IBuild[] = [];

      @lazyInject(TYPES.IBuildService)
      buildService: IBuildService;

      mount() {
        this.getBuilds();
      }

      private getBuilds() {
          //TODO
      }

  }

</script>

<style lang="scss" scoped>
  @import '../../main.scss';

  
</style>