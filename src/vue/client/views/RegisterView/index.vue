<template>
  <div class="registration-form">
    <div class="credentials-form">
      <h3 class="title">Credentials</h3>
      <credentials-form />
    </div>
    <hr />
    <div class="profile-form">
      <h3 class="title">Profile</h3>
      <profile-form />
    </div>
  </div>
</template>

<script>

import CredentialsForm from './../../components/CredentialsForm/index.vue';
import ProfileForm from './../../components/ProfileForm/index.vue';

export default {
  name: 'Register',
  components: {
    'credentials-form': CredentialsForm,
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

