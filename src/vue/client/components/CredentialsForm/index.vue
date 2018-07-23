<template>
  <div>
    <div class="field">
      <p class="control">
        <input class="input" type="email" placeholder="Email">
      </p>
    </div>
    <div class="field">
      <p class="control">
        <input class="input" type="password" placeholder="Password">
      </p>
    </div>
    <div class="field">
      <p class="control">
        <input class="input" type="password" placeholder="Password Confirm">
      </p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: false,
    }
  }
};
</script>

