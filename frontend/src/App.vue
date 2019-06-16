<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" class="app-nav">
      <b-navbar-brand href="#">CI Dashboard</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
          </b-navbar-nav>
        </b-collapse>
    </b-navbar>
    <b-container fluid>
      <b-row>
        <b-nav vertical class="app-nav sidebar col-md-1">
          <b-nav-text class="pl-3">Servers</b-nav-text>
          <b-nav-item class="pl-4" active>
            <i class="icon-travis-ci ci-logo"/>
             Travis CI
          </b-nav-item>
          <b-nav-item class="pl-4" active>
            <i class="icon-jenkins ci-logo"/>
             Jenkins
          </b-nav-item>
        </b-nav>
        <main role="main" class="col-md-11">
          <router-view />
        </main>
      </b-row>
    </b-container>
  </div>
</template>