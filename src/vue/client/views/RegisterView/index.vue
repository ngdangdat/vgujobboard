<template>
  <div class="registration-form">
    <profile-form @register="register"/>
  </div>
</template>

<script>

import ProfileForm from './../../components/ProfileForm/index.vue';
import { REGISTER_ACTIONS } from './../../constrains/user';

export default {
  name: 'Register',
  components: {
    'profile-form': ProfileForm,
  },
  methods: {
    register(payload) {
      console.log(payload);
      this.$store.dispatch(REGISTER_ACTIONS.REGISTER_REQUEST, payload);
    },
  }
};
</script>

<style lang="scss">
  .registration-form {
    width: 50%;
    margin: 0 auto;
  }
</style>

