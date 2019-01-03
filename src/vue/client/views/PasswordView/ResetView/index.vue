<template>
    <div class="reset-form">
        <h2 class="title has-text-centered is-3">
            Reset Password
        </h2>
        <div class="reset-form">
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
            <div class="buttons">
                <a @click="reset" class="button is-dark is-fullwidth">
                    Reset password
                </a>
            </div>
        </div>
    </div>
</template>

<script>
import Vue from 'vue';
import { mapGetters } from 'vuex';
import { PASSWORD_RESET_ACTIONS } from './../../../constrains/user';

const ResetView = Vue.extend({
    beforeMount() {
        if (this.user !== null) {
            this.$router.push('/password/reset');
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
            email: null,
        };
    },
    methods: {
        handleKeyEvents(e) {
            switch(e.keyCode) {
                case 13:
                    this.reset();
                    break;
                default:
                    break;
            }
        },
        reset() {
            this.$validator.validate().then(result => {
                if (result) {
                    this.$store.dispatch(PASSWORD_RESET_ACTIONS.PASSWORD_RESET, {
                        email: this.email,
                    });
                }
            });
        },
    },
   
})

export default ResetView;

</script>

<style lang="scss" scoped>
    .reset-form {
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

