import Vue from 'vue';

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
};

const MemberDetail = Vue.extend({
  props: {
    user: {
        type: Object,
        required: true,
    },
  },
  computed: {
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

export default MemberDetail;
