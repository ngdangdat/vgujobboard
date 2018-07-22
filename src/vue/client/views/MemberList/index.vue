<template>
  <div>
    <h2 class="title has-text-centered">
      VGU Alumni Member List
    </h2>
    <MemberList />
  </div>
</template>

<script>
import Vue from 'vue';
import MemberList from './../../components/MemberList/index.vue';

const MemberListView = Vue.extend({
  components: {
    MemberList, 
  },
});

export default MemberListView;
</script>
