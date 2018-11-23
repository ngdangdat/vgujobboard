<template>
  <div v-if="user">
    <div class="overview">
      <div class="avatar">
        <img :src="user.profile.avatar" :alt="fullName" />
      </div>
      <div class="column description">
        <p class="head">
          <strong>{{ fullName }}</strong>
        </p>
        <p class="sub">
          {{ `${getMajorDisplay(user.profile.major)}, ${user.profile.intake}` }}
        </p>
        <p class="sub">
          {{ `${getStateDisplay(user.profile.state)}, ${getCountryDisplay(user.profile.country)}` }}
        </p>
        <p class="sub">
          <a :href="`mailto:${user.email}`">{{ user.email }}</a>
        </p>
      </div>
    </div>
    <div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import { mapGetters } from 'vuex';
import { switchSnakeToCamelObj } from '@/utils/object.js';

const getMajorDisplay = (major) => {
    const mapping = {
        3: "Electrical Engineering and Information Technology",
        5: "Finance and Accounting",
    };
    return mapping[major];
};

const getStateDisplay = (state) => {
    const mapping = {
        HCM: "Ho Chi Minh City",
        HN: "Hanoi City",
    };
    return mapping[state];
};

const getCountryDisplay = (country) => {
    const mapping = {
        VN: "Vietnam",
        DE: "Germany",
    };
    return mapping[country];
}

const ProfileView = Vue.extend({
  name: 'ProfileView',
  computed: {
    ...mapGetters({
        user: 'user',
    }),
    fullName() {
        return `${this.user.first_name} ${this.user.last_name}`
    },
  },
  methods: {
      getMajorDisplay: (major) => getMajorDisplay(major),
      getCountryDisplay: (country) => getCountryDisplay(country),
      getStateDisplay: (state) => getStateDisplay(state),
  },
});

export default ProfileView;
</script>

<style lang="scss" scoped>
  .overview {
    align-items: center;
    display: flex;
    .avatar {
      img {
        max-height: 180px;
      }
    }
    .description {
      font-size: 1.2rem;
      line-height: 1.2;
      margin-left: 1rem;
      .head {
        font-size: 1.5em;
      }
    }
  }
  section {
    &:not(:first-child) {
      padding-top: 0;
    }
    &.work, &.education {
      .list {
        border: solid 1px;
        padding: 1rem;
        > li {
          padding: 1rem;
          &:not(:last-child) {
            border-bottom: solid 1px #ccc;
          }
        }
      }
    }
  }
</style>
