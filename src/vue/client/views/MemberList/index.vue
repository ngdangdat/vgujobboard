<template>
  <div>
    <h2 class="title has-text-centered">
      VGU Alumni Member List
    </h2>
    <ul style="width: 100%;" class="columns is-multiline">
      <li
        class="column is-half"
        v-for="(member, idx) in memberList"
        :key="idx"
      >
        <router-link :to="`/member/${member.id}`">
          <member-list-each :user="member" />
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import Vue from 'vue';
import { mapGetters } from 'vuex';
import MemberListEach from '@/components/MemberListEach/index.vue';
import { MEMBER_LIST_ACTIONS } from '@/constrains/member';

const MemberListView = Vue.extend({
  components: {
    'member-list-each': MemberListEach,
  },
  beforeMount() {
    let page = 1;
    const pageQuery = this.$route.query.page;
    if (typeof pageQuery !== 'undefined' && !isNaN(pageQuery)) {
      page = Number(pageQuery);
    }
    this.$store.dispatch(MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST, { page });
  },
  data() {
    return {
      
    };
  },
  computed: {
    ...mapGetters({
    currentPage: 'currentMemberPage',
    totalMembers: 'totalMembers',
    totalPages: 'totalMemberPages',
    }),
    memberList() {
      return this.getMembersByPage(this.currentPage);
    },
  },
  methods: {
    getMembersByPage(page) {
      return this.$store.getters.getMembersByPage(page);
    },
  },
});

export default MemberListView;
</script>

<style lang="scss">
  
</style>

