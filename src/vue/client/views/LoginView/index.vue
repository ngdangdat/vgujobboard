<template>
    <div class="login-form">
        <h2 class="title has-text-centered is-3">
            Login to VGU Alumni
        </h2>
        <span v-if="loginErrors">
            <span class="help is-danger" v-for="(value, key) in loginErrors" :key="key">{{ value }}</span>
        </span>
        <div class="login-form">
            <div class="field">
                <p class="control">
                    <input
                        v-validate="'email|required:true'"
                        placeholder="Email"
                        v-model="email"
                        name="email"
                        :class="{
                            'is-danger': errors.has('email')
                        }"
                        type="text"
                        class="input"
                    />
                    <span class="help is-danger">{{ errors.first('email') }}</span>
                </p>
            </div>
            <div class="field">
                <p class="control">
                    <input
                        v-validate="'required:true'"
                        placeholder="Password"
                        v-model="password"
                        name="password"
                        :class="{
                            'is-danger': errors.has('password')
                        }"
                        type="password"
                        class="input"
                    />
                    <span class="help is-danger">{{ errors.first('password') }}</span>
                </p>
            </div>
            <div class="forgot-block has-text-right">
                <a href="#">Forgot password?</a>
            </div>
            <div class="buttons">
                <a @click="login" class="button is-dark is-fullwidth">
                    Login
                </a>
                <div class="register">
                    <p class="has-text-centered">Don't have account? <router-link to="/register">Register now</router-link></p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Vue from 'vue';
import { mapGetters } from 'vuex';
// import USER_ACTIONS from './../../constrains/user';

const LoginView = Vue.extend({
    data() {
        return {
            email: null,
            password: null,
        };
    },
    computed: {
        ...mapGetters({
            loginErrors: 'loginErrors',
        }),
    },
    methods: {
        login() {
            this.$store.dispatch('login', {
                email: this.email,
                password: this.password,
            });
        },
    },
});

export default LoginView;

</script>

<style lang="scss" scoped>
    .login-form {
        width: 60%;
        margin: 0 auto;
        .forgot-block {
            margin-bottom: .5em;
        }
        .buttons {
            .register {
                width: 100%;
            }
            .button {
                margin-left: 0;
                margin-right: 0;
            }
        }
    }
</style>

