import { mapGetters } from 'vuex';

import FontAwesomeIcon from '@/components/FontAwesomeIcon/index.vue';
import DateSelectBox from '@/components/forms/DateSelectBox/index.vue';

import { REGISTER_ACTIONS } from '@/constrains/user';
import { COUNTRY_ACTIONS, CITY_ACTIONS } from '@/constrains/country';

import { getBase64Image } from '@/utils/image.js';

const parseDate = (date) => `${date.getFullYear()}-${date.getMonth()+1}-${date.getDate()}`;

export default {
  name: 'Register',
  beforeMount() {
    this.$store.commit(REGISTER_ACTIONS.REGISTER_REQUEST_RESET);
    this.$store.dispatch(COUNTRY_ACTIONS.COUNTRY_LIST_REQUEST);
  },
  data() {
    return {
      email: "", //string
      emailConfirm: "", //string
      gender: null, //number
      firstName: "", //string
      lastName: "", //string
      password: "", //string
      passwordConfirm: "", //string
      phoneNumber: "", //string
      major: null, //number
      intake: null, //number
      country: null, //string
      city: null, //string
      status: "", //string
      organization: "", //string
      title: "", //string
      birthday: null, //date
      avatar: null,
      avatarDisplay: null,
      availableMajors: [],
      availableIntakes: [],
    };
  },
  components: {
    'icon': FontAwesomeIcon,
    "date-select": DateSelectBox,
  },
  methods: {
    register() {
      this.$validator.validate().then(result => {
        if (result) {
          const avatar = this.avatar;
          let payload = {};
          const user = {
            "email": this.email,
            "password": this.password,
            "first_name": this.firstName,
            "last_name": this.lastName,
          };
          const profile = {
            "gender": this.gender,
            "major": this.major,
            "intake": this.intake,
            "phone_number": this.phoneNumber,
            "birthday": parseDate(this.birthday),
            "city": this.city,
            "country": this.country,
            "organization": this.organization,
            "title": this.title,
            "status": this.status,
          };
          payload["user"] = user;
          payload["profile"] = profile;
          payload["avatar"] = avatar.file;
        this.$store.dispatch(REGISTER_ACTIONS.REGISTER_REQUEST, payload);
        }
      });
    },
    changeBirthday(date) {
      this.birthday = date;
    },
    handleAvatarChange(e) {
      const imgFile = this.$refs.avatar.files[0];
      if (imgFile) {
        getBase64Image(imgFile)
          .then(avatarDisplay => {
            this.avatarDisplay = avatarDisplay;
            this.avatar = {
              'name': imgFile.name,
              'url': '',
              'file': imgFile,
            };
          })
      } else {
        this.avatarDisplay = null;
        this.avatar = null;
      }
    },
    getCityList(countryId) {
        const payload = {
            countryId,
        }
        this.$store.dispatch(CITY_ACTIONS.CITY_LIST_BY_COUNTRY_REQUEST, payload);
    },
  },
  computed: {
    ...mapGetters({
      registerErrors: 'registerErrors',
      registerSuccess: 'registerSuccess',
      countryList: 'countryList',
    }),
    availableCities() {
        return this.$store.getters.getCitesByCountryId(this.country);
    }
  },
  watch: {
    country(value) {
        this.city = null;
        this.getCityList(value);
    },
  },
};