import axios from 'axios';
import _ from 'lodash';
import { joinUrl } from './../../utils/url';
import { getHeaders } from './../../utils/request';
import config from '@/config/project.config.js';
import { MEMBER_LIST_ACTIONS, MEMBER_DETAIL_ACTIONS } from '@/constrains/member';
import Vue from 'vue';

let state = {
    loadings: {},
    success: {},
    // Object { [memberId]: Objet(user) }
    membersByID: {},
    // Object { [pageIndex]: Array(IDs) }
    memberIDsByPage: {},
    totalMembers: 1,
    totalPages: 1,
    currentPage: 1,
    errors: {},
};

let mutations = {
    // Member detail mutations
    [MEMBER_DETAIL_ACTIONS.MEMBER_DETAIL_REQUEST_PENDING] (state) {
        Vue.set(state.loadings, MEMBER_DETAIL_ACTIONS.MEMBER_DETAIL_REQUEST, true);
    },
    [MEMBER_DETAIL_ACTIONS.MEMBER_DETAIL_REQUEST_SUCCESS] (state, payload = {}) {
        let { id, user } = payload;
        Vue.set(state.membersByID, id, user);
    },
    [MEMBER_DETAIL_ACTIONS.MEMBER_DETAIL_REQUEST_FAILED] (state, payload = {}) {
        Vue.set(state.errors, MEMBER_DETAIL_ACTIONS.MEMBER_DETAIL_REQUEST, payload);
    },

    // Member list mutations
    [MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST_PENDING] (state) {
        Vue.set(state.loadings, MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST, true);
    },
    [MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST_SUCCESS] (state, payload = {}) {
        Vue.set(state.loadings, MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST, false);
        const { current, num_pages, count, results } = payload;

        let userIdsOfCurrentPage = [];
        results.forEach(user => {
            userIdsOfCurrentPage.push(user.id);
            Vue.set(state.membersByID, user.id, user);
        });

        Vue.set(state, 'totalMembers', count);
        Vue.set(state, 'totalPages', num_pages);
        Vue.set(state.memberIDsByPage, current, userIdsOfCurrentPage);
        Vue.set(state, 'currentPage', current);
    },
    [MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST_FAILED] (state, payload = {}) {
        Vue.set(state.loadings, MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST, false);
        Vue.set(state.errors, MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST, payload);
    },
};

let actions = {
    // Member detail actions
    [MEMBER_DETAIL_ACTIONS.MEMBER_DETAIL_REQUEST] ({ commit }, payload) {
        const { userId } = payload;
        commit(MEMBER_DETAIL_ACTIONS.MEMBER_DETAIL_REQUEST_PENDING);
        return axios({
            method: 'get',
            headers: getHeaders(),
            url: joinUrl(config.API_ENDPOINT, `user/${userId}`),
        }).then(response => {
            if (response.data.success) {
                commit(MEMBER_DETAIL_ACTIONS.MEMBER_DETAIL_REQUEST_SUCCESS, {
                    id: userId,
                    user: response.data.data,
                });
            } else {
                commit(MEMBER_DETAIL_ACTIONS.MEMBER_DETAIL_REQUEST_FAILED, response.data.errors);
            }
        });
    },

    // Member list action
    [MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST] ({ commit }, payload) {
        const { page } = payload;
        commit(MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST_PENDING);
        return axios({
            method: 'get',
            headers: getHeaders(),
            url: joinUrl(config.API_ENDPOINT, `user?page_size=${config.PAGINATION_PAGE_SIZE}&page=${page}`),
        }).then(response => {
            if (response.data.success) {
                commit(MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST_SUCCESS, response.data.data);
            } else {
                commit(MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST_FAILED, response.data.errors);
            }
        });
    },
};

let getters = {
    // Member detail
    getMemberById: (state) => (userId) => state.membersByID[userId] || {},
    errorGetMemberDetail: (state) => state.errors[MEMBER_DETAIL_ACTIONS.MEMBER_DETAIL_REQUEST] || null,

    // Member list
    getMembersByPage: (state) => page => {
        let userIds = state.memberIDsByPage[page] || [];
        if (userIds.length > 0) {
            return userIds.map(userId => state.membersByID[userId]);
        }

        return [];
    },
    totalMemberPages: state => state.totalPages || 1,
    totalMembers: state => state.totalMembers || 1,
    currentMemberPage: state => state.currentPage || 1,
    errorGetMemberList: state => state.errors[MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST] || null,
};

export default  {
    state,
    mutations,
    actions,
    getters,
};
