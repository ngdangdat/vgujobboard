<template>
  <div>
    <div v-if="!  registerSuccess" class="registration-form">
      <profile-form
        @register="register"
        :registerErrors="registerErrors"
      />
    </div>
    <div v-else>
        <div class="message-success content has-text-centered">
          <div class="success-icon">
            <icon 
              name="check-circle"
              classes="is-green"
              size="5x"
            />
          </div>
          <div class="success-message content">
            <p>Your register information has been submitted successfully.</p>
            <p>Please wait for us to validate your profile. Thank you!</p>
          </div>
        </div>
    </div>
  </div>
</template>

<script>

import ProfileForm from './../../components/ProfileForm/index.vue';
import FontAwesomeIcon from '@/components/FontAwesomeIcon/index.vue';
import { mapGetters } from 'vuex';
import { REGISTER_ACTIONS } from './../../constrains/user';

export default {
  name: 'Register',
  beforeMount() {
    this.$store.commit(REGISTER_ACTIONS.REGISTER_REQUEST_RESET);
  },
  components: {
    'profile-form': ProfileForm,
    'icon': FontAwesomeIcon,
  },
  methods: {
    register(payload) {
      this.$store.dispatch(REGISTER_ACTIONS.REGISTER_REQUEST, payload);
    },
  },
  computed: {
    ...mapGetters({
      registerErrors: 'registerErrors',
      registerSuccess: 'registerSuccess',
    })
  },
};
</script>

<style lang="scss" scoped>
  .registration-form {
    width: 50%;
    margin: 0 auto;
  }

  .message-success {
    .success-icon {
      margin-bottom: 10px;
    }
    .success-message {
      font-size: 1.2em;
      p {
        margin-bottom: .5em;
      }
    }
  }
</style>

