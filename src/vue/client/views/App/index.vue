<template>
    <div id="app">
        <NavigationBar :isLoggedIn="false"></NavigationBar>
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
import NavigationBar from './../../components/NavigationBar/index.vue';
import Footer from './../../components/Footer/index.vue';

const App = Vue.extend({
    components: {
        NavigationBar,
        Footer,
    },
});

export default App;
</script>

<style src="./styles/components.scss" />
