<template>
    <div id="app">
        <NavigationBar :user="loggedInUser" @logout="logout"></NavigationBar>
        <div class="container">
            <section class="section">
                <router-view></router-view>
            </section>
            <Footer></Footer>
        </div>
    </div>
</template>

<script>
import Vue from 'vue';
import { mapGetters } from 'vuex';
import NavigationBar from './../../components/NavigationBar/index.vue';
import Footer from './../../components/Footer/index.vue';
import { PROFILE_ACTIONS } from './../../constrains/user';

const App = Vue.extend({
    components: {
        NavigationBar,
        Footer,
    },
    computed: {
        ...mapGetters({
            loggedInUser: 'loggedInUser',
        }),
    },
    mounted() {
        this.$store.dispatch(PROFILE_ACTIONS.PROFILE_REQUEST);
    },
    methods: {
        logout() {
            this.$store.dispatch('logout');
        },
    },
});

export default App;
</script>

<style src="./styles/components.scss"></style>
<style src="./styles/global.scss"></style>
