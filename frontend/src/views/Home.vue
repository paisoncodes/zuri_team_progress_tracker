<template>
  <div>
    <div class="flex flex-col text-center bg-white">
      <NavbarComponent/>
      <HomeContainer />
    </div>
    <Footer />
  </div>
</template>

<script>
import HomeContainer from '../components/HomeContainer.vue'
import Footer from '../components/Footer.vue'
import NavbarComponent from '../components/NavbarComponent.vue'

export default {
  components: { NavbarComponent, HomeContainer, Footer },
  name: 'Home',
}
</script>