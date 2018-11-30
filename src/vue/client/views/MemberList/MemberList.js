import Vue from 'vue';
import { mapGetters } from 'vuex';
import MemberListEach from '@/components/MemberListEach/index.vue';
import Pagination from '@/components/Pagination/index.vue';
import { MEMBER_LIST_ACTIONS } from '@/constrains/member';

const parsePage = (rawPage, def = 0) => {
  if (typeof rawPage !== 'undefined' && !isNaN(rawPage)) {
    return Number(rawPage);
  }
  return def;
};

const MemberListView = Vue.extend({
  components: {
    'member-list-each': MemberListEach,
    'pagination': Pagination,
  },
  beforeMount() {
    let page = 1;
    const pageQuery = this.$route.query.page;
    page = parsePage(pageQuery, page);

    this.getPageMember(page);
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
    getPageMember(page) {
      this.$store.dispatch(MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST, { page });
    },
    changePage(page) {
      this.getPageMember(page);
      if (typeof this.$route.query.page !== 'undefined' || page !== 1) {
        this.$router.push(`/member?page=${page}`)
      }
    },
  },
  watch: {
    $route(to, from) {
      let page = null;
      if (to.query.page !== from.query.page) {
        page = parsePage(to.query.page, 1);
        this.changePage(page);
      }
    },
  },
});

export default MemberListView;