<template>
  <div class="columns">
    <div class="column profile-form">
      <h3 class="title">Profile</h3>
      <profile-form />
    </div>
    <div class="column credentials-form is-one-quarter">
      <h3 class="title">Credentials</h3>
      <credentials-form />
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
