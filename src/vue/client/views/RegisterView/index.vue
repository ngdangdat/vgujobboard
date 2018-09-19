<template>
  <div class="registration-form">
    <profile-form @register="register"/>
  </div>
</template>

<script>

import ProfileForm from './../../components/ProfileForm/index.vue';

export default {
  name: 'Register',
  components: {
    'profile-form': ProfileForm,
  },
  methods: {
    register(payload) {
      this.$store.dispatch('register', payload);
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

