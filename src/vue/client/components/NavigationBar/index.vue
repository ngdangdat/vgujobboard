<template>
    <nav class="navbar is-spaced is-warning" role="navigation" aria-label="main navigation">
        <div class="nav-container container">
            <div class="navbar-brand">
                <a class="navbar-item" href="./">
                    <img
                        src="@/static/images/vgu_logo.png"
                        alt="Vietnamese-German University"
                    />
                </a>
                <div @click="changeMenuState"
                    class="navbar-burger burger"
                    :class="{
                        'is-active': isMenuActive,
                    }"
                >
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
            <div
                class="navbar-menu"
                :class="{
                    'is-active': isMenuActive,
                }"
            >
                <div class="navbar-start">
                    <router-link to="/" class="navbar-item bd-navbar-item-documentation">Home</router-link>
                    <a class="navbar-item bd-navbar-item-documentation"
                        href="https://www.facebook.com/VGUAlumniCommunity/"
                        target="_blank"
                    >
                        Facebook
                    </a>
                    <a class="navbar-item bd-navbar-item-documentation"
                        href="https://vgualumniqna.tumblr.com/"
                        target="_blank"
                    >
                        QnA
                    </a>
                </div>
                <div class="navbar-end">
                    <router-link v-if="user == null" to="/login" class="is-hidden-touch button">Login</router-link>
                    <div v-else class="is-hidden-touch dropdown is-hoverable is-right">
                        <div class="dropdown-trigger">
                            <div class="avatar is-hidden-touch button" aria-haspopup="true" aria-controls="account-menu">
                                <img :src="user.profile.avatar" :alt="user.name">
                            </div>
                            <div class="caret-down"></div>
                        </div>
                        <div class="dropdown-menu has-text-centered" id="account-menu" role="menu">
                            <div class="dropdown-content">
                                <div class="dropdown-item">
                                    <router-link to="/profile">
                                        Profile
                                    </router-link>
                                </div>
                                <div class="dropdown-item">
                                    <router-link to="/member">
                                        Members
                                    </router-link>
                                </div>
                                <div class="dropdown-item">
                                    <a href="#" @click="logout">Logout</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <router-link v-if="user == null" to="/login" class="navbar-item is-hidden-desktop">Login</router-link>
                    <div v-else>
                        <router-link class="navbar-item bd-navbar-item-documentation is-hidden-desktop" to="/profile">
                            Profile
                        </router-link>
                        <router-link class="navbar-item bd-navbar-item-documentation is-hidden-desktop" to="/member">
                            Members
                        </router-link>
                        <a href="#" class="navbar-item bd-navbar-item-documentation is-hidden-desktop" @click="logout">Logout</a>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
import Vue from "vue";

const NavigationBar = Vue.extend({
  name: "NavigationBar",
  props: {
    /**
     * Flag to check if user logged in
     */
    user: {
      type: Object,
      default: null,
      required: false
    }
  },
  data() {
    return {
      navItems: [
        {
          id: 0,
          index: 0,
          title: "Home",
          url: "/",
          external: false,
        },
        {
          id: 1,
          index: 1,
          title: "Facebook",
          url: "https://www.facebook.com/VGUAlumniCommunity/",
          external: true,
        },
        {
          id: 2,
          index: 2,
          title: "QnA",
          url: "https://vgualumniqna.tumblr.com/",
          external: true,
        }
      ],
      isMenuActive: false
    };
  },
  methods: {
    logout() {
      this.$emit("logout");
    },
    changeMenuState() {
      this.isMenuActive = !this.isMenuActive;
    }
  }
});

export default NavigationBar;
</script>

<style lang="scss" src="./style.scss" />
