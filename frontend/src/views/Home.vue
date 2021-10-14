<template>
  <div class="bg-red-100 ">
    <p class="text-center">This is the official page of the project tracker app</p>
    <HomeContainer />
  <div>
    <!--This is the official page of the project tracker app
    <HomeContainer />-->
    <NavbarComponent/>
  </div>
</template>

<script>
// import HomeContainer from '../components/HomeContainer.vue'
import NavbarComponent from '../components/NavbarComponent.vue'

export default {
  // components: { HomeContainer, NavbarComponent },
  components: {NavbarComponent },
  name: 'Home',
}
</script>
