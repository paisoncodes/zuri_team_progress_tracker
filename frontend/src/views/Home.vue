<template>
  <div class="text-center">
    This is the official page of the project tracker app
    <HomeContainer />
    <HomeContainer />
    <Footer />
  </div>
</template>

<script>
import HomeContainer from '../components/HomeContainer.vue'
import NavbarComponent from '../components/NavbarComponent.vue'
import Footer from '../components/Footer.vue'

export default {
  components: { HomeContainer,NavbarComponent, Footer },
  name: 'Home',
}
</script>
