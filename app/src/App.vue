<template>
  <div id="app">
    <Nav />
    <div class="container">
      <router-view/>
    </div>
  </div>
</template>

<script>
import Nav from '@/components/Nav'

export default {
  components: {
    Nav
  },
  created() {
    this.$store.dispatch('initialize')
  }
}
</script>
