<template>
    <div class="newpassword-form">
        <h2 class="title has-text-centered is-3">
            Login to VGU Alumni
        </h2>
        <div class="newpassword-form">
            <div class="field">
                <p class="control">
                    <input
                        v-model="password"
                        class="input"
                        :class="{
                          'is-danger':
                          errors.has('passwordConfirm')
                        }"
                        v-validate="'required:true|min:6'"
                        type="password"
                        placeholder="Password"
                        name="password"
                        ref="password"
                    />
                    <span class="help is-danger">{{ errors.first('password') }}</span>
                </p>
            </div>
            <div class="field">
                <p class="control">
                    <input
                        v-model="passwordConfirm"
                        class="input"
                        :class="{
                          'is-danger':
                          errors.has('passwordConfirm')
                        }"
                        v-validate="'required:true|confirmed:password'"
                        type="password"
                        placeholder="Password Confirm"
                        name="passwordConfirm"
                    />
                    <span class="help is-danger">{{ errors.first('passwordConfirm') }}</span>
                </p>
            </div>
            <div class="buttons">
                <a @click="login" class="button is-dark is-fullwidth">
                    Change password
                </a>
            </div>
        </div>
    </div>
</template>

<script>
import Vue from 'vue';
import { mapGetters } from 'vuex';
import { LOGIN_RESET_PASSWORD_ACTION } from './../../constrains/user';

const NewPasswordView = Vue.extend({
    beforeMount() {
        if (this.user !== null) {
            this.$router.push('/newpassword');
        }
    },
    mounted() {
        window.addEventListener('keydown', this.handleKeyEvents);
    },
    beforeDestroy() {
        window.removeEventListener('keydown', this.handleKeyEvents);
    },
    data() {
        return {
            password: null,
        };
    },
    methods: {
        handleKeyEvents(e) {
            switch(e.keyCode) {
                case 13:
                    this.login();
                    break;
                default:
                    break;
            }
        },
        login() {
            this.$validator.validate().then(result => {
                if (result) {
                    this.$store.dispatch(LOGIN_RESET_PASSWORD_ACTION.LOGIN_RESET_PASSWORD, {
                        password: this.password,
                    });
                }
            });
        },
    },
    watch: {
        PasswordSuccess(val) {
            if(val) {
                this.$router.push('/');
            }
        }
    },
})

export default NewPasswordView;

</script>

<style lang="scss" scoped>
    .newpassword-form {
        max-width: 350px;
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
