import Vue from 'vue';
import Router from 'vue-router';

import Home from '../views/Home/index.vue';
import MemberList from '../views/MemberList/index.vue';
import MemberDetail from '../views/MemberDetail/index.vue';
import Profile from '../views/Profile/index.vue';
import Register from '../views/RegisterView/index.vue';
import Login from '../views/LoginView/index.vue';
import ResetPassword from '../views/PasswordView/ResetView/index.vue';
import ChangePassword from '../views/PasswordView/ChangeView/index.vue';
import PasswordDone from '../views/PasswordView/DoneView/index.vue';

Vue.use(Router);

const router = new Router({
    mode: 'hash',
    routes: [
        {
            path: '/',
            component: Home,
            meta: {
                requiresAuth: false,
            },
        },
        {
            path: '/member',
            component: MemberList,
            meta: {
                requiresAuth: true,
            },
        },
        {
            path: '/member/:userId',
            component: MemberDetail,
            props: true,
            meta: {
                requiresAuth: true,
            },
        },
        {
            path: '/register',
            component: Register,
            meta: {
                requiresAuth: false,
            },
        },
        {
            path: '/login',
            component: Login,
            meta: {
                requiresAuth: false,
            },
        },
        {
            path: '/profile',
            component: Profile,
            props: true,
            meta: {
                requiresAuth: true,
            },
        },
        {
            path: '/password/reset',
            component: ResetPassword,
            props: true,
            meta: {
                requiresAuth: false,
            },
        },
        {
            path: '/password/new',
            component: ChangePassword,
            props: true,
            meta: {
                requiresAuth: false, //change to TRUE for token after testing
            },
        },
        {
            path: '/password/done',
            component: PasswordDone,
            props: true,
            meta: {
                requiresAuth: false,
            },
        },
    ],
});

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (localStorage.getItem('token') == null) {
            next({
                path: '/login',
            });
        } else {
            next();
        }
    } else {
        next();
    }
});

export default router;
