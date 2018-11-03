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
import { mapGetters } from 'vuex';
import MemberList from './../../components/MemberList/index.vue';

const MemberListView = Vue.extend({
  components: {
    MemberList, 
  },
  computed: {
    ...mapGetters({
      pagination: 'memberListPagination',
    }),
    currentMemberList() {
      
    },
  },
});

export default MemberListView;
</script>
