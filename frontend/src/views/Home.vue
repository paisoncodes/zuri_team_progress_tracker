<template>
  <div>
    <div class="bg-white text-center flex flex-col">
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