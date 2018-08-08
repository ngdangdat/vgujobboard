<template>
    <nav class="navbar is-spaced is-warning" role="navigation" aria-label="main navigation">
        <div class="nav-container container">
            <div class="navbar-brand">
                <a class="navbar-item" href="./">
                    <img
                        src="http://vgu.edu.vn/cms-vgu-theme-4/images/cms/vgu_logo.png"
                        alt="Vietnamese-German University"
                    />
                </a>
                <div class="navbar-burger burger">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
            <div class="navbar-menu">
                <router-link v-for="navItem in navItems"
                    :to="navItem.url"
                    :key="navItem.id"
                    class="navbar-item"
                >
                    {{ navItem.title }}
                </router-link>
            </div>
            <div class="navbar-menu secondary">
                <router-link v-if="!isLoggedIn" to="/login" class="button">Login</router-link>
                <div v-else class="dropdown is-hoverable is-right">
                    <div class="dropdown-trigger">
                        <div class="avatar" aria-haspopup="true" aria-controls="account-menu">
                            <img src="https://unsplash.it/160/160" :alt="user.name">
                        </div>
                        <div class="caret-down"></div>
                    </div>
                    <div class="dropdown-menu has-text-centered" id="account-menu" role="menu">
                        <div class="dropdown-content">
                            <div class="dropdown-item">
                                <a href="#">Account</a>
                            </div>
                            <div class="dropdown-item">
                                <a href="#">Account</a>
                            </div>
                            <hr class="dropdown-divider">
                            <div class="dropdown-item">
                                <router-link to="/member">
                                    Members
                                </router-link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'NavigationBar',
    props: {
        /**
         * Flag to check if user logged in
         */
        isLoggedIn: {
            type: Boolean,
            default: false,
        },
        /**
         * Object contains user information
         */
        user: {
            type: Object,
            default: () => {
                return {
                    name: 'Dat Nguyen',
                };
            },
        }
    },
    data() {
        return {
            navItems: [
                {
                    id: 0,
                    index: 0,
                    title: 'Home',
                    url: '/',
                },
                {
                    id: 1,
                    index: 1,
                    title: 'Facebook',
                    url: '/',
                },
                {
                    id: 2,
                    index: 2,
                    title: 'QnA',
                    url: '/',
                },
            ],
        };
    },
};
</script>

<style src="./style.scss" />
