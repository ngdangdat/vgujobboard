<template>
  <div>
    <member-detail
      v-if="memberDetail"
      :user="memberDetail"
    />
    <div v-else class="error">
      Can't find this user. Back to <router-link to="/member">user list</router-link>.
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import { MEMBER_DETAIL_ACTIONS } from '@/constrains/member.js';
import { mapGetters } from 'vuex';
import MemberDetailComponent from '@/components/Member/index.vue';

const MemberDetailView = Vue.extend({
  props: ['userId'],
  components: {
    'member-detail': MemberDetailComponent,
  },
  beforeMount() {
    this.$store.dispatch(MEMBER_DETAIL_ACTIONS.MEMBER_DETAIL_REQUEST, {
      userId: this.userId,
    });
  },
  computed: {
    ...mapGetters({
      getMemberErrors: 'getMemberErrors',
    }),
    memberDetail() {
      const memberDetail = this.$store.getters.getMemberById(this.userId);
      if (typeof memberDetail === "object" && Object.keys(memberDetail).length > 0) {
        return memberDetail;
      }
      return null;
    },
  },
  watch: {
    userId(value, oldValue) {
      if (value !== oldValue) {
        this.$forceUpdate();
      }
    }
  },
});

export default MemberDetailView;
</script>
