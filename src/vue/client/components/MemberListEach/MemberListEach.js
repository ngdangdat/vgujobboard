import Vue from 'vue';

const MemberListEach = Vue.extend({
  props: {
    user: {
      type: Object,
      required: true,
    },
  },
  mounted() {

  },
  data() {
    return {

    };
  },
  computed: {
    fullName() {
      return `${this.user.first_name} ${this.user.last_name}`;
    },
  },
});

export default MemberListEach;
