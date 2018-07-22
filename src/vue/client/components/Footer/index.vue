<template>
  <div class="footer">
      <div class="content has-text-centered">
          <p>
              <span><strong>Vietnamese-German University Alumni Team 2018</strong> &copy;.</span>
              <span>Contact us at: <a :href="`mailto:${email}`">{{ email }}</a></span>
          </p>
      </div>
  </div>
</template>

<script>
import Vue from 'vue';

const FooterComponent = Vue.extend({
  data() {
    return {
      email: 'vgu.alumni@gmail.com',
    };
  }
});

export default FooterComponent;
</script>

