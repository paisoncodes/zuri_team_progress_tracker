<template>
  <div class="text-center">
    <div class="bg-brand-gray-light-2">This is the official page of the project tracker app</div> 
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
