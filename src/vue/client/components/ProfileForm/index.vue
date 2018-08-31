<template>
  <div>
    <h2 class="title has-text-centered is-3">
        Registration Form
    </h2>
    <div class="form">
      <div class="field">
        <p class="control">
          <input class="input" type="email" placeholder="Email">
        </p>
      </div>
      <div class="field two-cols">
        <p class="col control">
          <input class="input" type="password" placeholder="Password">
        </p>
        <p class="col control">
          <input class="input" type="password" placeholder="Password Confirm">
        </p>
      </div>
      <div class="three-cols fields">
        <div class="field col">
          <p class="control">
            <input class="input" type="text" placeholder="First Name">
          </p>
        </div>
        <div class="field col">
          <p class="control">
            <input class="input" type="text" placeholder="Last Name">
          </p>
        </div>
        <div class="field col">
          <div class="control">
            <div class="select full-width">
              <select>
                <option value="">Gender</option>
                <option value="1">Male</option>
                <option value="3">Female</option>
              </select>
            </div>
          </div>
        </div>
      </div>
      <div class="field">
        <p class="control">
          <input class="input" type="text" placeholder="Phone Number (optional)">
        </p>
      </div>
      <div class="field">
        <div class="three-cols control">
          <div class="col select full-width">
            <select>
              <option value="">Date of birth</option>
            </select>
          </div>
          <div class="col select full-width">
            <select>
              <option value="">Date of birth</option>
            </select>
          </div>
          <div class="col select full-width">
            <select>
              <option value="">Date of birth</option>
            </select>
          </div>
        </div>
      </div>
      <div class="field">
        <div class="control two-cols">
          <div class="col select full-width">
            <select>
              <option value="">Major</option>
              <option value="1">EEIT</option>
              <option value="3">FA</option>
            </select>
          </div>
          <div class="col select full-width">
            <select>
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
            <select>
              <option value="">Current Country of Residence</option>
              <option value="VN">Vietnam</option>
              <option value="DE">Germany</option>
            </select>
          </div>
          <div class="col select full-width">
            <select>
              <option value="">Current City of Residence</option>
              <option value="HCM">Ho Chi Minh</option>
              <option value="HN">Ha Noi</option>
            </select>
          </div>
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
              Image for avatar
            </span>
          </span>
          <span class="file-name">
            Screen Shot 2017-07-29 at 15.54.25.png
          </span>
        </label>
      </div>
    </div>
    <div class="btns">
      <a class="button is-halfwidth">
        Back
      </a>
      <a class="button is-dark is-halfwidth">
        Next
      </a>
    </div>
  </div>
</template>

<style lang="scss" scoped>
  .three-cols, .two-cols{
    display: flex;
    justify-content: space-between;
  }
  .three-cols .col {
    width: 32%;
  }
  .two-cols .col {
    width: 49%;
  }
  .form {
    margin-bottom: 1em;
  }
  .btns {
    text-align: right;
    a.button {
      min-width: 10rem;
    }
  }
</style>

