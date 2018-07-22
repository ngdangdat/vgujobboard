import Vue from 'vue';
import App from './views/App/index.vue';
import store from './store';
import router from './router';

let app = new Vue({
  store,
  router,
  render: h => h(App),
});

export { app };
