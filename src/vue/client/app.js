import Vue from 'vue';
import App from './views/App/index.vue';
import store from './store';
import router from './router';

// Validator for forms
import VeeValidate, { Validator } from 'vee-validate';
import en from './components/forms/VeeValidator/dicts/en';
import '@/static/css/bulma.css';
import '@/styles/components.scss';
import '@/styles/global.scss';

Validator.localize(en);

Vue.use(VeeValidate, {
  events: 'blur|change',
});

let app = new Vue({
  store,
  router,
  render: h => h(App),
});

export { app };
