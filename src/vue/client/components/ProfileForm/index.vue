<template>
  <div>
    <h2 class="title has-text-centered is-3">
        Registration Form
    </h2>
    <div v-if="registerErrors" class="errors message is-danger">
        <div class="message-body">
            <li class="help" v-for="(errorMsg, errorCode) in registerErrors" :key="errorCode">
                <span>{{ errorMsg }}</span>
            </li>
        </div>
    </div>
    <div class="form">
      <div class="field">
        <div class="control two-cols">
          <div class="col">
            <input name="email"
              v-validate="'email|required'"
              v-model="email"
              class="input"
              :class="{
                'is-danger': errors.has('email'),
              }"
              type="email"
              placeholder="Email"
              ref="email"
            >
            <span class="help is-danger">{{ errors.first('email') }}</span>
          </div>
          <div class="col">
            <input v-model="emailConfirm"
              class="input"
              :class="{
                'is-danger': errors.has('emailConfirm'),
              }"
              type="email"
              name="emailConfirm"
              placeholder="Email Confirm"
              v-validate="'confirmed:email|required'"
              
            >
            <span class="help is-danger">{{ errors.first('emailConfirm') }}</span>
          </div>
        </div>
      </div>
      <div class="field">
        <div class="two-cols">
          <div class="col control">
            <input
              v-model="password"
              class="input"
              :class="{
                'is-danger': errors.has('passwordConfirm')
              }"
              v-validate="'required:true|min:6'"
              type="password"
              placeholder="Password"
              name="password"
              ref="password"
            >
            <span class="help is-danger">{{ errors.first('password') }}</span>
          </div>
          <div class="col control">
            <input
              v-model="passwordConfirm"
              class="input"
              :class="{
                'is-danger': errors.has('passwordConfirm')
              }"
              v-validate="'required:true|confirmed:password'"
              type="password"
              placeholder="Password Confirm"
              name="passwordConfirm"
            >
            <span class="help is-danger">{{ errors.first('passwordConfirm') }}</span>
          </div>
        </div>
      </div>
      <hr />
      <div class="field">
        <date-select
          date-label='Date of Birth'
          month-label='Month of Birth'
          year-label='Year of Birth'
          v-validate="'required:true'"
          v-model="birthday"
          name="birthday"
          @change="changeBirthday"
          :value="birthday"
          :error="errors.has('birthday')"
        />
        <span class="help is-danger">{{ errors.first('birthday') }}</span>
      </div>
      <div class="two-cols fields">
        <div class="field col">
          <p class="control">
            <input v-model="firstName" v-validate="'required:true'"
              :class="{
                'is-danger': errors.has('firstName')
              }"
              class="input"
              type="text"
              name="firstName"
              placeholder="First Name"
            >
            <span class="help is-danger">{{ errors.first('firstName') }}</span>
          </p>
        </div>
        <div class="field col">
          <p class="control">
            <input v-model="lastName" v-validate="'required:true'"
              name="lastName"
              :class="{
                'is-danger': errors.has('lastName')
              }"
              class="input"
              type="text"
              placeholder="Last Name"
            >
            <span class="help is-danger">{{ errors.first('lastName') }}</span>
          </p>
        </div>
      </div>
      <div class="field two-cols">
        <div class="col">
          <div class="select full-width">
            <select v-model="gender"
              name="gender"
              v-validate="'required:true'"
              class="input"
              :class="{
                'is-danger': errors.has('gender')
              }"
            >
              <option :value="null">Gender</option>
              <option :value="1">Male</option>
              <option :value="3">Female</option>
              <option :value="5">Other(s)</option>
            </select>
          </div>
          <span class="help is-danger">{{ errors.first('gender') }}</span>
        </div>
        <div class="control col">
          <input v-model="phoneNumber"
            name="phoneNumber"
            class="input"
            :class="{
              'is-danger': errors.has('phoneNumber'),
            }"
            v-validate="'numeric'"
            type="text"
            placeholder="Phone Number (optional)"
          >
          <span class="help is-danger">{{ errors.first('phoneNumber') }}</span>
        </div>
      </div>
      <div class="field">
        <div class="control two-cols">
          <div class="col">
            <div class="select full-width">
              <select v-model="major"
                v-validate="'required:true'"
                class="input"
                :class="{
                  'is-danger': errors.has('major')
                }"
                name="major"
              >
                <option :value="null">Major</option>
                <option :value="3">EEIT</option>
                <option :value="5">FA</option>
                <!-- <option v-for="(eachMajor, index) in availableMajors" :key="index" :value="eachMajor.value">
                  {{ eachMajor.display }}
                </option> -->
              </select>
            </div>
            <span class="help is-danger">{{ errors.first('major') }}</span>
          </div>
          <div class="col">
            <div class="select full-width">
              <select v-model="intake"
                name="intake"
                v-validate="'required:true'"
                class="input"
                :class="{
                  'is-danger': errors.has('intake')
                }"
              >
                <option :value="null">Intake</option>
                <option :value="2011">2011</option>
                <option :value="2012">2012</option>
                <!-- <option v-for="(eachIntake, index) in availableIntakes" :key="index" :value="eachIntake.value">
                  {{ eachIntake.display }}
                </option> -->
              </select>
            </div>
            <span class="help is-danger">{{ errors.first('intake') }}</span>
          </div>
        </div>
      </div>
      <div class="field">
        <div class="control two-cols">
          <div class="col">
            <div class="select full-width">
              <select v-model="country"
                name="country"
                v-validate="'required:true'"
                class="input"
                :class="{
                  'is-danger': errors.has('country')
                }"
              >
                <option :value="null">Current Country of Residence</option>
                <option value="VN">Vietnam</option>
                <option value="DE">Germany</option>
                <!-- <option v-for="(eachCountry, index) in availableCountries" :key="index" :value="eachCountry.value">
                  {{ eachCountry.display }}
                </option> -->
              </select>
            </div>
            <span class="help is-danger">{{ errors.first('country') }}</span>
          </div>
          <div class="col">
            <div class="select full-width">
              <select v-model="state"
                name="state"
                v-validate="'required:true'"
                class="input"
                :class="{
                  'is-danger': errors.has('state')
                }"
              >
                <option :value="null">Current City of Residence</option>
                <option value="HCM">Ho Chi Minh</option>
                <option value="HN">Ha Noi</option>
                <!-- <option v-for="(eachState, index) in availableStates" :key="index" :value="eachState.value">
                  {{ eachState.display }}
                </option> -->
              </select>
            </div>
            <span class="help is-danger">{{ errors.first('state') }}</span>
          </div>
        </div>
      </div>
      <div class="field">
        <div class="control">
          <input v-model="organization"
            name="organization"
            v-validate="'required:true'"
            class="input"
            :class="{
              'is-danger': errors.has('organization')
            }"
            type="text"
            placeholder="Current company/university"
          >
          <span class="help is-danger">{{ errors.first('organization') }}</span>
        </div>
      </div>
      <div class="field">
        <div class="control">
          <input v-model="title"
            name="title"
            v-validate="'required:true'"
            class="input"
            :class="{
              'is-danger': errors.has('title')
            }"
            type="text"
            placeholder="Current position/major"
          >
          <span class="help is-danger">{{ errors.first('title') }}</span>
        </div>
      </div>
      <div class="field">
        <div class="control">
          <textarea v-model="status"
            name="status"
            class="textarea"
            type="text"
            placeholder="Message to VGU"
          />
        </div>
      </div>
      <div class="field">
        <div v-if="avatarDisplay">
          <img :src="avatarDisplay" alt="Avatar">
        </div>
        <div class="file has-name is-fullwidth is-right">
          <label class="file-label">
            <input class="file-input" v-validate="'required|image'"
              ref="avatar"
              type="file"
              name="avatar"
              @change="handleAvatarChange"
            />
            <span class="file-cta">
              <span class="file-icon">
                <icon v-if="avatar" name="times" />
                <icon v-else name="upload" />
              </span>

              <span v-if="avatar" class="file-label">Clear</span>
              <span v-else class="file-label">Profile picture</span>
            </span>
            <span v-if="avatar" class="file-name">
              {{ avatar.name }}
            </span>
          </label>
        </div>
        <span class="help is-danger">{{ errors.first('avatar') }}</span>
      </div>
    </div>
    <div class="btns">
      <a class="is-dark button is-halfwidth" @click="register">Register</a>
    </div>
  </div>
</template>

<script>
import DateSelectBox from "@/components/forms/DateSelectBox/index.vue";
import FontAwesomeIcon from "@/components/FontAwesomeIcon/index.vue";
import { getBase64Image } from '@/utils/image.js';
import Vue from "vue";

import countries from '@/mock/country.json';
import majors from '@/mock/major.json';

const parseDate = (date) => `${date.getFullYear()}-${date.getMonth()+1}-${date.getDate()}`;

const ProfileForm = Vue.extend({
  components: {
    "date-select": DateSelectBox,
    "icon": FontAwesomeIcon,
  },
  props: {
    registerErrors: {
      type: Object,
    },
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
      state: null, //string
      status: "", //string
      organization: "", //string
      title: "", //string
      birthday: null, //date
      avatar: null,
      avatarDisplay: null,
      availableCountries: countries,
      availableStates: [],
      availableMajors: majors,
      availableIntakes: [],
    };
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
            "state": this.state,
            "country": this.country,
            "organization": this.organization,
            "title": this.title,
            "status": this.status,
          };
          payload["user"] = user;
          payload["profile"] = profile;
          payload["avatar"] = avatar.file;
        this.$emit("register", payload);
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
    }
  },
  watch: {
  //   country(value) {
  //     this.state = null;
  //     if (value) {
  //       const selectedCountry = this.availableCountries.find(country => country.value === value);
  //       this.availableStates = selectedCountry.childrens;
  //       return;
  //     }
  //     this.availableStates = [];
  //   },
  //   major(value) {
  //     this.intake = null;
  //     if (value) {
  //       const selectedMajor = this.availableMajors.find(major => major.value === value);
  //       this.availableIntakes = selectedMajor.childrens;
  //       return;
  //     }
  //     this.availableIntakes = [];
  //   },
  },
});

export default ProfileForm;
</script>
