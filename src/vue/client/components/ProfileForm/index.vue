<template>
  <div>
    <h2 class="title has-text-centered is-3">
        Registration Form
    </h2>
    <div class="form">
      <div class="field">
        <div class="control two-cols">
          <input v-model="email" class="input col" type="email" placeholder="Email">
          <input v-model="emailConfirm" class="input col" type="email" placeholder="Email Confirm">
        </div>
      </div>
      <div class="field two-cols">
        <p class="col control">
          <input v-model="password" class="input" type="password" placeholder="Password">
        </p>
        <p class="col control">
          <input v-model="passwordConfirm" class="input" type="password" placeholder="Password Confirm">
        </p>
      </div>
      <hr />
      <div class="field">
        <date-select
          date-label='Date of Birth'
          month-label='Month of Birth'
          year-label='Year of Birth'
          @change="changeBirthday"
        />
      </div>
      <div class="two-cols fields">
        <div class="field col">
          <p class="control">
            <input v-model="firstName" class="input" type="text" placeholder="First Name">
          </p>
        </div>
        <div class="field col">
          <p class="control">
            <input v-model="lastName" class="input" type="text" placeholder="Last Name">
          </p>
        </div>
      </div>
      <div class="field two-cols">
        <div class="select col full-width">
          <select v-model="gender">
            <option value="">Gender</option>
            <option value="1">Male</option>
            <option value="3">Female</option>
            <option value="5">Other(s)</option>
          </select>
        </div>
        <p class="control col">
          <input v-model="phoneNumber" class="input" type="text" placeholder="Phone Number (optional)">
        </p>
      </div>
      <div class="field">
        <div class="control two-cols">
          <div class="col select full-width">
            <select v-model="major">
              <option value="">Major</option>
              <option value="1">EEIT</option>
              <option value="3">FA</option>
            </select>
          </div>
          <div class="col select full-width">
            <select v-model="intake">
              <option value="">Intake</option>
              <option value="2011">2011</option>
              <option value="2012">2012</option>
            </select>
          </div>
        </div>
      </div>
      <div class="field">
        <div class="control two-cols">
          <div class="col select full-width">
            <select v-model="country">
              <option value="">Current Country of Residence</option>
              <option value="VN">Vietnam</option>
              <option value="DE">Germany</option>
            </select>
          </div>
          <div class="col select full-width">
            <select v-model="state">
              <option value="">Current City of Residence</option>
              <option value="HCM">Ho Chi Minh</option>
              <option value="HN">Ha Noi</option>
            </select>
          </div>
        </div>
      </div>
      <div class="field">
        <p class="control">
          <input v-model="organization" class="input" type="text" placeholder="Current company/university">
        </p>
      </div>
      <div class="field">
        <p class="control">
          <input v-model="title" class="input" type="text" placeholder="Current position/major">
        </p>
      </div>
      <div class="field">
        <div class="control">
          <textarea v-model="status" class="textarea" type="text" placeholder="Message to VGU"></textarea>
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

const ProfileForm = Vue.extend({
  components: {
    "date-select": DateSelectBox
  },
  data() {
    return {
      email: "",
      emailConfirm: "",
      gender: "",
      firstName: "",
      lastName: "",
      password: "",
      passwordConfirm: "",
      phoneNumber: "",
      major: "",
      intake: "",
      country: "",
      state: "",
      status: "",
      organization: "",
      title: "",
      birthday: null,
    };
  },
  methods: {
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
        birthday: this.birthday,
        state: this.state,
        country: this.country,
        organization: this.organization,
        title: this.title,
        status: this.status
      };
      payload["profile"] = profile;
      this.$emit("register", {});
    },
    changeBirthday(selectedDate) {
      this.birthday = selectedDate;
    },
  }
});

export default ProfileForm;
</script>
