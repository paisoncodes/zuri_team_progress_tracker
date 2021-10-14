<template>
  <div class="text-center">
    This is the official page of the project tracker app
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
