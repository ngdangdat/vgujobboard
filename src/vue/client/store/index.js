import Vue from 'vue';
import Vuex from 'vuex';
import user from './modules/user';
import member from './modules/member';
import country from './modules/country';
import major from './modules/major';

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        user,
        member,
        country,
        major,
    },
});