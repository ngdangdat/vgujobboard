<template>
  <div>
    <member-detail
      v-if="user"
      :user="user"
    />
  </div>
</template>

<script>
import Vue from 'vue';
import { mapGetters } from 'vuex';
import MemberDetailComponent from '@/components/Member/index.vue';

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
  components: {
    'member-detail': MemberDetailComponent,
  },
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
