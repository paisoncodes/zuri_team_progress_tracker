<template>
  <div class="bg-white text-center flex content-center">
    <HomeContainer />
    <Footer />
  </div>
</template>

<script>
import HomeContainer from '../components/HomeContainer.vue'
import Footer from '../components/Footer.vue'

export default {
  components: { HomeContainer, Footer },
  name: 'Home',
}
</script>
