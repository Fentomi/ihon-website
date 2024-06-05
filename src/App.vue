<template>
  <Authorization
    v-if="!userIsAuthorized"
    :user-is-authorized="userIsAuthorized"
    @updateUserIsAuthorized="userIsAuthorized=true"
  />
</template>

<style>
</style>

<script>
import Authorization from '@/components/Authorization.vue';

export default {
  name: 'App',
  components: {
    Authorization,
  },
  data() {
    return {
      userIsAuthorized: false,
    }
  }
}
</script>
