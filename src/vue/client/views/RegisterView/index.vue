<template>
  <div class="registration-form">
    <profile-form />
  </div>
</template>

<script>

import CredentialsForm from './../../components/CredentialsForm/index.vue';
import ProfileForm from './../../components/ProfileForm/index.vue';

export default {
  name: 'Register',
  components: {
    'profile-form': ProfileForm,
  },
};
</script>

<style lang="scss">
  .registration-form {
    width: 50%;
    margin: 0 auto;
  }
</style>

