import axios from 'axios';
import _ from 'lodash';
import { joinUrl } from './../../utils/url';
import { getHeaders } from './../../utils/request';
import config from './../../../config/project.config';
import { LOGIN_ACTIONS, PROFILE_ACTIONS, LOGOUT_ACTIONS } from './../../constrains/user';

const state = {
    loading: false,
    user: null,
};

const mutations = {
    [LOGIN_ACTIONS.LOGIN_PENDING] (state) {
        state.loading = true;
    },
    [LOGIN_ACTIONS.LOGIN_SUCCESS] (state, payload = {}) {
        state.loading = false;
        if (payload.token !== undefined) {
            localStorage.setItem('token', payload.token);
        }
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
        commit(LOGIN_ACTIONS.LOGIN_PENDING);
        return axios({
            method: 'post',
            headers: getHeaders(),
            url: joinUrl(config.API_ENDPOINT, 'auth'),
            data: payload,
        })
        .then(response => commit(LOGIN_ACTIONS.LOGIN_SUCCESS, response.data.data))
        .then(() => dispatch('getUserProfile'));
    },
    logout({ commit }, payload) {
        state.user = null;
        localStorage.removeItem('token');
    }
};

const getters = {
    loggedInUser: state => state.user || null,
    isUserLoading: state => state.loading || false,
};

export default {
    state,
    mutations,
    actions,
    getters,
};
