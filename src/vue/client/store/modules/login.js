import axios from 'axios';
import { joinUrl } from './../../utils/url';
import { getHeaders } from './../../utils/request';
import config from './../../../config/project.config';
import LOGIN_ACTIONS from './../../constrains/user';

const state = {
    loggedIn: false,
    loading: false,
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
};

const actions = {
    login({ commit }, payload) {
        commit(LOGIN_ACTIONS.LOGIN_PENDING);
        console.log(getHeaders());
        return axios({
            method: 'post',
            options: {
                headers: getHeaders(),
            },
            headers: getHeaders(),
            url: `${config.API_ENDPOINT}/auth`,
            data: payload,
        }).then(
            response => {
                if (window.localStorage) {
                    commit(LOGIN_ACTIONS.LOGIN_SUCCESS, response.data);
                }
            }
        );
    },
};

const getters = {
    loggedIn: state => state.loggedIn || false,
};

export default {
    state,
    mutations,
    actions,
    getters,
};
