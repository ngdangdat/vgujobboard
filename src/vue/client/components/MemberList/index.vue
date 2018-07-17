<template>
  <ul style="width: 100%;" class="columns is-multiline">
    <li
      class="column is-half"
      v-for="user in users"
      :key="user.id"
      @click="viewUser(user.id)"
    >
        <div class="user-card">
          <img :src="user.avatar" :alt="user.name"/>
          <div class="info">
            <p><strong>{{ user.name }}</strong></p>
            <p>{{ `${user.major} ${user.year}` }}</p>
            <p>{{ user.currentWork }}</p>
            <p>{{ `${user.city}, ${user.country}` }}</p>
          </div>
        </div>
    </li>
  </ul>
</template>

<script>
import Vue from 'vue';

const userList = [
  {
    id: 0,
    name: 'Hung Dong',
    year: 2011,
    major: 'EEIT',
    currentWork: 'Software Engineer at Renesat',
    avatar: 'https://unsplash.it/200/200',
    city: 'HCMC',
    country: 'Vietnam',
  },
  {
    id: 1,
    name: 'Truc Lam',
    year: 2011,
    major: 'FA',
    currentWork: 'Unemployee at somewhere in Earth',
    avatar: 'https://unsplash.it/200/200',
    city: 'HCMC',
    country: 'Vietnam',
  },
  {
    id: 2,
    name: 'Luan Le',
    year: 2011,
    major: 'FA',
    currentWork: 'Unemployee at somewhere in Earth',
    avatar: 'https://unsplash.it/200/200',
    city: 'HCMC',
    country: 'Vietnam',
  },
  {
    id: 3,
    name: 'Hao Nguyen',
    year: 2011,
    major: 'FA',
    currentWork: 'Unemployee at somewhere in Earth',
    avatar: 'https://unsplash.it/200/200',
    city: 'HCMC',
    country: 'Vietnam',
  },
];

const MemberList = Vue.extend({
  mounted() {
    this.users = userList;
  },
  methods: {
    viewUser: (id) => {
      this.$router.push(`/member/${id}`);
    },
  },
  data() {
    return {
      users: [],
    };
  },
});

export default MemberList;
</script>

<style src="./style.scss" lang="scss" />

