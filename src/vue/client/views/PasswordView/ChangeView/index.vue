<template>
    <div class="change-form">
        <h2 class="title has-text-centered is-3">
            Lorem Ipsum
        </h2>
        <div class="change-form">
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
                <a @click="change" class="button is-dark is-fullwidth">
                    Change password
                </a>
            </div>
        </div>
    </div>
</template>

<script>
import Vue from 'vue';
import { mapGetters } from 'vuex';
import { PASSWORD_CHANGE_ACTIONS } from './../../../constrains/user';

const ChangeView = Vue.extend({
    beforeMount() {
        if (this.user !== null) {
            this.$router.push('/password/new');
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
                    this.change();
                    break;
                default:
                    break;
            }
        },
        change() {
            this.$validator.validate().then(result => {
                if (result) {
                    this.$store.dispatch(PASSWORD_CHANGE_ACTIONS.PASSWORD_CHANGE, {
                        password: this.password,
                    });
                }
            });
        },
    },
    watch: {
        ChangeSuccess(val) {
            if(val) {
                this.$router.push('/done');
            }
        }
    },
})

export default ChangeView;

</script>

<style lang="scss" scoped>
    .change-form {
        max-width: 350px;
        margin: 0 auto;
        .forgot-block {
            margin-bottom: .5em;
        }
        .buttons {
            .button {
                margin-left: 0;
                margin-right: 0;
            }
        }
    }
</style>
