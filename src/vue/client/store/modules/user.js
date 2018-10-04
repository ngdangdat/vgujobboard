import axios from 'axios';
import _ from 'lodash';
import { joinUrl } from './../../utils/url';
import { getHeaders } from './../../utils/request';
import config from './../../../config/project.config';
import { LOGIN_ACTIONS, PROFILE_ACTIONS, REGISTER_ACTIONS } from './../../constrains/user';
import Vue from 'vue';

const state = {
    loadings: {},
    user: null,
    errors: {},
};

const mutations = {
    [LOGIN_ACTIONS.LOGIN_REQUEST_PENDING] (state) {
        Vue.set(state.loadings, LOGIN_ACTIONS.LOGIN_REQUEST, true);
    },
    [LOGIN_ACTIONS.LOGIN_REQUEST_SUCCESS] (state, payload = {}) {
        Vue.set(state.loadings, LOGIN_ACTIONS.LOGIN_REQUEST, false);
        if (payload.token !== undefined) {
            // Consider using session
            localStorage.setItem('token', payload.token);
        }
    },
    [LOGIN_ACTIONS.LOGIN_REQUEST_FAILED] (state, payload = {}) {
        Vue.set(state.loadings, LOGIN_ACTIONS.LOGIN_REQUEST, false);
        Vue.set(state.errors, LOGIN_ACTIONS.LOGIN_REQUEST, payload);
    },
    [PROFILE_ACTIONS.PROFILE_REQUEST_PENDING] (state) {
        state.loading = true;
    },
    [PROFILE_ACTIONS.PROFILE_REQUEST_SUCCESS] (state, payload = {}) {
        state.loading = false;
        if (payload.user !== undefined) {
            const { user } = payload;
            state.user = user;
        }
    },
    [REGISTER_ACTIONS.REGISTER_REQUEST_PENDING] (state) {
        state.loading = true;
    },
    [REGISTER_ACTIONS.REGISTER_REQUEST_SUCCESS] (state) {
        state.loading = false;
    },
};

const actions = {
    getUserProfile({ commit }) {
        commit(PROFILE_ACTIONS.PROFILE_REQUEST_PENDING);
        return axios({
            method: 'get',
            headers: getHeaders(),
            url: joinUrl(config.API_ENDPOINT, 'user/profile'),
        }).then(
            response => {
                commit(PROFILE_ACTIONS.PROFILE_REQUEST_SUCCESS, {
                    user: response.data.data,
                });
            }
        );
    },
    login({ commit, dispatch }, payload) {
        commit(LOGIN_ACTIONS.LOGIN_REQUEST_PENDING);
        return axios({
            method: 'post',
            headers: getHeaders(),
            url: joinUrl(config.API_ENDPOINT, 'auth'),
            data: payload,
        })
            .then(response => {
                if (response.success) {
                    commit(LOGIN_ACTIONS.LOGIN_REQUEST_SUCCESS, response.data.data);
                    dispatch('getUserProfile');
                } else {
                    commit(LOGIN_ACTIONS.LOGIN_REQUEST_FAILED, response.data.errors);
                }
            });
    },
    logout({ commit }, payload) {
        state.user = null;
        localStorage.removeItem('token');
    },
    register({ commit, dispatch }, payload) {
        commit(REGISTER_ACTIONS.REGISTER_REQUEST_PENDING);
        return axios({
            method: 'post',
            headers: getHeaders(),
            url: joinUrl(config.API_ENDPOINT, 'user'),
            data: payload,
        })
            .then(() => commit(REGISTER_ACTIONS.REGISTER_REQUEST_SUCCESS))
    },
};

const getters = {
    loginErrors: state => state.errors[LOGIN_ACTIONS.LOGIN_REQUEST] || null,
    loggedInUser: state => state.user || null,
    isUserLoading: state => state.loading || false,
};

export default {
    state,
    mutations,
    actions,
    getters,
};
