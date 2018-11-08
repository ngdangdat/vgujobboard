import axios from 'axios';
import _ from 'lodash';
import { joinUrl } from './../../utils/url';
import { getHeaders } from './../../utils/request';
import config from './../../../config/project.config';
import { LOGIN_ACTIONS, PROFILE_ACTIONS, REGISTER_ACTIONS, MEMBER_LIST_ACTIONS } from './../../constrains/user';
import Vue from 'vue';

const state = {
    loadings: {},
    user: null,
    success: {},
    errors: {},
    pathBeforeLogin: null,
    membersListPagination: {},
    membersByPage: [],
    membersCurrentPage: [],
};

const mutations = {
    // Login mutations
    [LOGIN_ACTIONS.LOGIN_REQUEST_PENDING] (state) {
        Vue.set(state.loadings, LOGIN_ACTIONS.LOGIN_REQUEST, true);
    },
    [LOGIN_ACTIONS.LOGIN_REQUEST_SUCCESS] (state, payload = {}) {
        Vue.set(state.loadings, LOGIN_ACTIONS.LOGIN_REQUEST, false);
        Vue.set(state.errors, LOGIN_ACTIONS.LOGIN_REQUEST, null);
        Vue.set(state.success, LOGIN_ACTIONS.LOGIN_REQUEST, true);
        if (payload.token !== undefined) {
            // Consider using session
            // MUST USE SESSION
            localStorage.setItem('token', payload.token);
        }
    },
    [LOGIN_ACTIONS.LOGIN_REQUEST_FAILED] (state, payload = {}) {
        Vue.set(state.loadings, LOGIN_ACTIONS.LOGIN_REQUEST, false);
        Vue.set(state.errors, LOGIN_ACTIONS.LOGIN_REQUEST, payload);
    },
    [PROFILE_ACTIONS.PROFILE_REQUEST_PENDING] (state) {
        Vue.set(state.loadings, PROFILE_ACTIONS.PROFILE_REQUEST, true);
    },
    [PROFILE_ACTIONS.PROFILE_REQUEST_SUCCESS] (state, payload = {}) {
        Vue.set(state.loadings, PROFILE_ACTIONS.PROFILE_REQUEST, false);
        if (payload.user !== undefined) {
            const { user } = payload;
            Vue.set(state, 'user', user);
        }
    },

    // Register mutations
    [REGISTER_ACTIONS.REGISTER_REQUEST_PENDING] (state) {
        Vue.set(state.loadings, REGISTER_ACTIONS.REGISTER_REQUEST, true);
    },
    [REGISTER_ACTIONS.REGISTER_REQUEST_SUCCESS] (state) {
        Vue.set(state.loadings, REGISTER_ACTIONS.REGISTER_REQUEST, false);
    },
    [REGISTER_ACTIONS.REGISTER_REQUEST_FAILED] (state, payload = {}) {
        Vue.set(state.loadings, REGISTER_ACTIONS.REGISTER_REQUEST, false);
        Vue.set(state.errors, REGISTER_ACTIONS.REGISTER_REQUEST, payload);
    },

    // Member list mutations
    [MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST_PENDING] (state) {
        Vue.set(state.loadings, MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST, true);
    },
    [MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST_SUCCESS] (state, payload = {}) {
        Vue.set(state.loadings, MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST, false);
        const { current, num_pages, count, results } = payload;
        const pageIndex = current - 1;
        Vue.set(state, 'membersListPagination', Object.assign({}, {
            totalPage: num_pages,
            count: count,
            currentPage: current,
        }));
        Vue.set(state.membersByPage, pageIndex, results);
    },
    [MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST_FAILED] (state, payload = {}) {
        Vue.set(state.loadings, MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST, false);
        Vue.set(state.errors, MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST, payload);
    },
    [MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST_CHANGE_PAGE] (state, payload = {}) {
        Vue.set()
    }
};

const actions = {
    [PROFILE_ACTIONS.PROFILE_REQUEST] ({ commit }) {
        commit(PROFILE_ACTIONS.PROFILE_REQUEST_PENDING);
        return axios({
            method: 'GET',
            headers: getHeaders(),
            url: joinUrl(config.API_ENDPOINT, 'user/profile'),
        }).then(
            response => {
                if (response.data.success) {
                    commit(PROFILE_ACTIONS.PROFILE_REQUEST_SUCCESS, {
                        user: response.data.data,
                    });
                }
            }
        );
    },
    [LOGIN_ACTIONS.LOGIN_REQUEST] ({ commit, dispatch }, payload) {
        commit(LOGIN_ACTIONS.LOGIN_REQUEST_PENDING);
        axios({
            method: 'POST',
            headers: getHeaders(),
            url: joinUrl(config.API_ENDPOINT, 'auth'),
            data: payload,
        }).then(response => {
            if (response.data.success) {
                commit(LOGIN_ACTIONS.LOGIN_REQUEST_SUCCESS, response.data.data);
                dispatch(PROFILE_ACTIONS.PROFILE_REQUEST);
            } else {
                commit(LOGIN_ACTIONS.LOGIN_REQUEST_FAILED, response.data.errors);
            }
        });
    },
    logout({ commit }, payload) {
        state.user = null;
        localStorage.removeItem('token');
    },
    [REGISTER_ACTIONS.REGISTER_REQUEST]  ({ commit }, payload) {
        commit(REGISTER_ACTIONS.REGISTER_REQUEST_PENDING);
        let formData = new FormData();
        const { profile, user, avatar } = payload;

        for (let key in profile) {
            let val = profile[key];
            formData.append(`profile.${key}`, val);
        }

        for (let key in user) {
            let val = user[key];
            formData.append(`${key}`, val);
        }

        formData.append('profile.avatar', avatar, 'test.png');
        console.log('avatar', avatar);
        console.log('avatar keys', Object.keys(avatar));
        
        let headers = {
            'Content-Type': 'multipart/form-data',
        };

        console.log(formData);

        return axios({
            method: 'post',
            headers: headers,
            url: joinUrl(config.API_ENDPOINT, 'user'),
            data: formData,
        }).then(response => {
            if (response.data.success) {
                commit(REGISTER_ACTIONS.REGISTER_REQUEST_SUCCESS, response.data.data);
            } else {
                commit(REGISTER_ACTIONS.REGISTER_REQUEST_FAILED, response.data.errors);
            }
        });
    },
    [MEMBER_LIST_ACTIONS.MEMBER_LIST_REQUEST] ({ commit }, payload) {
        let page = 1;
        if (Object.keys(payload).indexOf('page') > -1 && payload.page) {
            page = payload.page;
        }
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

const getters = {
    loginErrors: state => state.errors[LOGIN_ACTIONS.LOGIN_REQUEST] || null,
    loginSuccess: state => state.success[LOGIN_ACTIONS.LOGIN_REQUEST] || false,
    registerErrors: state => state.errors[REGISTER_ACTIONS.REGISTER_REQUEST] || null,
    loggedInUser: state => state.user || null,
    isUserLoading: state => state.loading || false,
    membersByPage: state => page => state.membersByPage[page] || [],
    membersListPagination: state => state.membersListPagination || Object.assign({}, {
        totalPage: 1,
        count: 1,
        currentPage: 1,
    }),
};

export default {
    state,
    mutations,
    actions,
    getters,
};
