import Vue from "vue";
import BootstrapVue from 'bootstrap-vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faClock } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import App from "./App.vue";
import router from "./router";
import './assets/css/dashboard.css';
import './main.scss';

Vue.config.productionTip = false;
Vue.use(BootstrapVue);

library.add(faClock)

Vue.component('fa-icon', FontAwesomeIcon);

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
