<template>
  <div class="flex flex-col text-center bg-white">
    <NavbarComponent/>
    <HomeContainer />
    <Footer1 />
  </div>
</template>

<script>
import HomeContainer from '../components/HomeContainer.vue'
import Footer1 from '../components/Footer1.vue'
import NavbarComponent from '../components/NavbarComponent.vue'

export default {
  components: { NavbarComponent, HomeContainer, Footer1 },
  name: 'Home',
}
</script>