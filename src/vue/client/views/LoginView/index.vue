<template>
    <div class="login-form">
        <h2 class="title has-text-centered is-3">
            Login to VGU Alumni
        </h2>
        <div class="login-form">
            <div class="field">
                <p class="control">
                    <input placeholder="Email" type="text" class="input">
                </p>
            </div>
            <div class="field">
                <p class="control">
                    <input placeholder="Password" type="password" class="input">
                </p>
            </div>
            <div class="forgot-block has-text-right">
                <a href="#">Forgot password?</a>
            </div>
            <div class="buttons">
                <a class="button is-dark is-fullwidth">
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

const LoginView = Vue.extend({
    
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

