import Vue from 'vue';
import Router from 'vue-router';

import Home from '../views/Home/index.vue';
import MemberList from '../views/MemberList/index.vue';
import Member from '../views/Member/index.vue';

Vue.use(Router);

const router = new Router({
    mode: 'hash',
    routes: [
        {
            path: '/',
            component: Home,
        },
        {
            path: '/member',
            component: MemberList,
        },
        {
            path: '/member/:id',
            component: Member,
            props: true,
        },
    ],
});

export default router;
