import axios from 'axios';
import Vue from 'vue';
import { joinUrl } from '@/utils/url';
import { getHeaders } from '@/utils/request';
import config from '@/config/project.config.js';
import { CITY_ACTIONS, COUNTRY_ACTIONS } from '@/constrains/country.js';


let state = {
    loadings: {},
    errors: {},
    countries: [],
    citiesByCountry: {},
};

const mutations = {
    [COUNTRY_ACTIONS.COUNTRY_LIST_REQUEST_PENDING] (state) {
        Vue.set(state.loadings, COUNTRY_ACTIONS.COUNTRY_LIST_REQUEST, true);
    },
    [COUNTRY_ACTIONS.COUNTRY_LIST_REQUEST_SUCCESS] (state, payload = {}) {
        Vue.set(state.loadings, COUNTRY_ACTIONS.COUNTRY_LIST_REQUEST, false);
        const { countries } = payload;
        Vue.set(state, 'countries', countries);
    },

    [CITY_ACTIONS.CITY_LIST_BY_COUNTRY_REQUEST_PENDING] (state) {
        Vue.set(state.loadings, COUNTRY_ACTIONS.CITY_LIST_BY_COUNTRY_REQUEST, true);
    },
    [CITY_ACTIONS.CITY_LIST_BY_COUNTRY_REQUEST_SUCCESS] (state, payload = {}) {
        Vue.set(state.loadings, COUNTRY_ACTIONS.CITY_LIST_BY_COUNTRY_REQUEST, false);
        const { countryId, cities } = payload;
        Vue.set(state.citiesByCountry, countryId, cities);
    },
};

const actions = {
    [COUNTRY_ACTIONS.COUNTRY_LIST_REQUEST] ({ commit }) {
        commit(COUNTRY_ACTIONS.COUNTRY_LIST_REQUEST_PENDING);
        return axios({
            method: 'GET',
            headers: getHeaders(),
            url: joinUrl(config.API_ENDPOINT, 'user/country'),
        }).then(response => {
            if (response.data.success) {
                commit(COUNTRY_ACTIONS.COUNTRY_LIST_REQUEST_SUCCESS, {
                    countries: response.data.data,
                });
            } else {
                // Handle errors
            }
        });
    },
    [CITY_ACTIONS.CITY_LIST_BY_COUNTRY_REQUEST] ({commit}, payload) {
        const { countryId } = payload;
        commit(CITY_ACTIONS.CITY_LIST_BY_COUNTRY_REQUEST_PENDING);

        return axios({
            method: 'GET',
            headers: getHeaders(),
            url: joinUrl(config.API_ENDPOINT, `user/country/${countryId}/cities`),
        }).then(response => {
            if (response.data.success) {
                commit(CITY_ACTIONS.CITY_LIST_BY_COUNTRY_REQUEST_SUCCESS, {
                    countryId: countryId,
                    cities: response.data.data,
                });
            } else {
                // Handle errors
            }
        });
    }
};

const getters = {
    countryList: state => state.countries || [],
    getCitesByCountryId: state => countryId => state.citiesByCountry[countryId] || [],
};

export default {
    state,
    mutations,
    actions,
    getters,
};
