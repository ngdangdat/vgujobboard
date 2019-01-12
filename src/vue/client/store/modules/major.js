import Vue from 'vue';
import axios from 'axios';
import { MAJOR_LIST_ACTIONS } from '@/constrains/major.js';
import { joinUrl } from '@/utils/url';
import { getHeaders } from '@/utils/request';
import config from '@/config/project.config.js';

let state = {
    loadings: {},
    success: {},
    errors: {},
    majorList: [],
};

let mutations = {
    [MAJOR_LIST_ACTIONS.MAJOR_REQUEST_LIST_PENDING] (state) {
        Vue.set(state.loadings, MAJOR_LIST_ACTIONS.MAJOR_REQUEST_LIST, true);
    },
    [MAJOR_LIST_ACTIONS.MAJOR_REQUEST_LIST_SUCCESS] (state, payload) {
        const { majorList } = payload;
        Vue.set(state.loadings, MAJOR_LIST_ACTIONS.MAJOR_REQUEST_LIST, false);
        Vue.set(state.success, MAJOR_LIST_ACTIONS.MAJOR_REQUEST_LIST, true);
        Vue.set(state.errors, MAJOR_LIST_ACTIONS.MAJOR_REQUEST_LIST, null);
        Vue.set(state, 'majorList', majorList);
    },
    [MAJOR_LIST_ACTIONS.MAJOR_REQUEST_LIST_FAILED] (state, payload) {
        const { errors } = payload;
        Vue.set(state.errors, MAJOR_LIST_ACTIONS.MAJOR_REQUEST_LIST, errors);
    },
};

let actions = {
    [MAJOR_LIST_ACTIONS.MAJOR_REQUEST_LIST] ({ commit }, payload) {
        return axios({
            method: 'GET',
            headers: getHeaders(),
            url: joinUrl(config.API_ENDPOINT, 'user/major'),
        }).then(response => {
            if (response.data.success) {
                commit(MAJOR_LIST_ACTIONS.MAJOR_REQUEST_LIST_SUCCESS, { majorList: response.data.data, });
            } else {
                commit(MAJOR_LIST_ACTIONS.MAJOR_REQUEST_LIST_SUCCESS, { errors: response.data.errors, });
            }
        });
    },
};

let getters = {
    isMajorGetLoading: state => state.loadings[MAJOR_LIST_ACTIONS.MAJOR_REQUEST_LIST] || false,
    majorGetErrors: state => state.errors[MAJOR_LIST_ACTIONS.MAJOR_REQUEST_LIST] || [],
    majorList: state => state.majorList || [],
};

export default {
    state,
    mutations,
    actions,
    getters,
};
