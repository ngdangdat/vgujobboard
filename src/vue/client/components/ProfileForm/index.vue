<template>
  <div>
    <h2 class="title has-text-centered is-3">
        Registration Form
    </h2>
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
            v-validate="'required:false'"
            class="textarea"
            type="text"
            placeholder="Message to VGU"
          />
        </div>
      </div>
      <div class="file has-name is-fullwidth">
        <label class="file-label">
          <input class="file-input" type="file" name="resume">
          <span class="file-cta">
            <span class="file-icon">
              <i class="fas fa-upload"></i>
            </span>
            <span class="file-label">
              Profile picture
            </span>
          </span>
          <span class="file-name">
            Screen Shot 2017-07-29 at 15.54.25.png
          </span>
        </label>
      </div>
    </div>
    <div class="btns">
      <!-- <a class="button is-halfwidth">
        Back
      </a>
      <a class="button is-dark is-halfwidth">
        Next
      </a> -->
      <a class="is-dark button is-halfwidth" @click="register">Register</a>
    </div>
  </div>
</template>

<script>
import DateSelectBox from "../forms/DateSelectBox/index.vue";
import Vue from "vue";
import Datepicker from "vuejs-datepicker";

const parseDate = (date) => `${date.getFullYear()}-${date.getMonth()}-${date.getDate()}`;

const ProfileForm = Vue.extend({
  components: {
    "date-select": DateSelectBox
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
    };
  },
  methods: {
    validate() {
        
    },
    register() {
      // @TODO: Validation
      let payload = {};
      payload["email"] = this.email;
      payload["password"] = this.password;
      payload["first_name"] = this.firstName;
      payload["last_name"] = this.lastName;
      const profile = {
        gender: this.gender,
        major: this.major,
        intake: this.intake,
        phone_number: this.phoneNumber,
        birthday: parseDate(this.birthday),
        state: this.state,
        country: this.country,
        organization: this.organization,
        title: this.title,
        status: this.status,
      };
      payload["profile"] = profile;
      this.$emit("register", payload);
    },
    changeBirthday(date) {
      this.birthday = date;
    },
  }
});

export default ProfileForm;
</script>
