<template>
  <div v-if="member">
    <div class="overview">
      <div class="avatar">
        <img :src="member.avatarUrl" :alt="`${member.firstName} ${member.lastName}`" />
      </div>
      <div class="column description">
        <p class="head">
          <strong>{{ `${member.firstName} ${member.lastName}` }}</strong>
        </p>
        <p class="sub">
          {{ `${member.major} ${member.year}` }}
        </p>
        <p class="sub">
          {{ `${member.city}, ${member.country}` }}
        </p>
        <p class="sub">
          {{ member.email }}
        </p>
      </div>
    </div>
    <div>
      <section v-if="member.works" class="section work">
        <h3 class="title">Work</h3>
        <ul class="list">
          <li v-for="work in member.works" :key="work.id">
            <p>
              <strong>{{ work.title }}</strong>
            </p>
            <p>{{ work.company }}</p>
            <p>{{ `${work.from} - ${work.to || 'Present'}` }}</p>
            <p>{{ work.description }}</p>
          </li>
        </ul>
      </section>
      <section v-if="member.educations" class="section education">
        <h3 class="title">Education</h3>
        <ul class="list">
          <li v-for="education in member.educations" :key="education.id">
            <p><strong>{{ education.title }}</strong></p>
            <p>{{ education.company }}</p>
            <p>{{ `${education.from} - ${education.to || 'Present'}` }}</p>
            <p>{{ education.description }}</p>
          </li>
        </ul>
      </section>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';

const members = [
  {
    id: 0,
    email: 'hung.dong@gmail.com',
    firstName: 'Hung',
    lastName: 'Dong',
    year: 2011,
    major: 'EEIT',
    currentWork: 'Software Engineer at Renesat',
    avatarUrl: 'https://unsplash.it/160/160',
    city: 'HCMC',
    country: 'Vietnam',
    works: [
      {
        id: 0,
        from: 2012,
        to: 2016,
        title: 'Student',
        company: 'Vietnamese-German University',
        description: 'Be a greater man'
      },
      {
        id: 1,
        from: 2016,
        to: null,
        title: 'Software Engineer',
        company: 'Renesat',
        description: 'Create bugs and fix bugs'
      },
    ],
    educations: [
      {
        id: 0,
        from: 2012,
        to: 2016,
        title: 'Student',
        company: 'Vietnamese-German University',
        description: 'Be a greater man'
      },
    ],
  },
];

const MemberView = Vue.extend({
  props: ['id'],
  computed: {
    member() {
      return members.find(member => member.id == this.id);
    },
  },
  parseWork() {
    let works = this.member.works;
  }
});

export default MemberView;
</script>

<style lang="scss" scoped>
  .overview {
    align-items: center;
    display: flex;
    .description {
      font-size: 1.2rem;
      line-height: 1.2;
      margin-left: 1rem;
      .head {
        font-size: 1.5em;
      }
    }
  }
  section {
    &:not(:first-child) {
      padding-top: 0;
    }
    &.work, &.education {
      .list {
        border: solid 1px;
        padding: 1rem;
        > li {
          padding: 1rem;
          &:not(:last-child) {
            border-bottom: solid 1px #ccc;
          }
        }
      }
    }
  }
</style>

