import axios from 'axios';
import _ from 'lodash';
import { joinUrl } from './../../utils/url';
import { getHeaders } from './../../utils/request';
import config from '@/config/project.config.js';
import { LOGIN_ACTIONS, PROFILE_ACTIONS, REGISTER_ACTIONS } from './../../constrains/user';
import Vue from 'vue';

const state = {
    loadings: {},
    user: null,
    success: {},
    errors: {},
    pathBeforeLogin: null,
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
    [REGISTER_ACTIONS.REGISTER_REQUEST_RESET] (state) {
        Vue.set(state.success, REGISTER_ACTIONS.REGISTER_REQUEST, false);
    },
    [REGISTER_ACTIONS.REGISTER_REQUEST_PENDING] (state) {
        Vue.set(state.loadings, REGISTER_ACTIONS.REGISTER_REQUEST, true);
    },
    [REGISTER_ACTIONS.REGISTER_REQUEST_SUCCESS] (state) {
        Vue.set(state.loadings, REGISTER_ACTIONS.REGISTER_REQUEST, false);
        Vue.set(state.errors, REGISTER_ACTIONS.REGISTER_REQUEST, null);
        Vue.set(state.success, REGISTER_ACTIONS.REGISTER_REQUEST, true);
    },
    [REGISTER_ACTIONS.REGISTER_REQUEST_FAILED] (state, payload = {}) {
        Vue.set(state.loadings, REGISTER_ACTIONS.REGISTER_REQUEST, false);
        Vue.set(state.errors, REGISTER_ACTIONS.REGISTER_REQUEST, payload);
    },
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
        const { user, avatar } = payload;

        const userJsonData = JSON.stringify(user);

        formData.append('user', userJsonData);
        formData.append('profile.avatar', avatar);
        let headers = {
            'Content-Type': 'multipart/form-data',
        };

        window.test = formData;
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
};

const getters = {
    loginErrors: state => state.errors[LOGIN_ACTIONS.LOGIN_REQUEST] || null,
    loginSuccess: state => state.success[LOGIN_ACTIONS.LOGIN_REQUEST] || false,
    registerErrors: state => state.errors[REGISTER_ACTIONS.REGISTER_REQUEST] || null,
    registerSuccess: state => state.success[REGISTER_ACTIONS.REGISTER_REQUEST] || false,
    loggedInUser: state => state.user || null,
    isUserLoading: state => state.loading || false,
    user: state => state.user || null,
};

export default {
    state,
    mutations,
    actions,
    getters,
};
