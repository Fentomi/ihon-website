<template>
  <Authorization
    v-if="!userIsAuthorized"
    :user-is-authorized="userIsAuthorized"
    @updateUserIsAuthorized="userIsAuthorized=true"
  />
  <Main
    v-if="userIsAuthorized"
    @logout="userIsAuthorized=false"
  />
</template>

<script>
import Authorization from '@/components/Authorization.vue';
import Main from '@/components/Main.vue';

export default {
  name: 'App',
  components: {
    Authorization,
    Main,
  },
  data() {
    return {
      userIsAuthorized: true,
    }
  }
}
</script>

<style>
.wrapper {
  margin: 30vh auto;
  width: 600px;
}
</style>