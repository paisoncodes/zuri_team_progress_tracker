<template>
  <div>
    <div class="bg-white text-center flex flex-col">
      <HeaderNavbar/>
      <TestContainer class="padTop"/>
    </div>
    <Footer />
  </div>
</template>

<script>
// import NavbarComponent from '../components/NavbarComponent.vue'
import HeaderNavbar from '../components/HeaderNavComponent.vue'
// import Subscribe from "../components/Subscribe.vue"
import TestContainer from '../components/TabContainer.vue'
import Footer from '../components/Footer.vue'

export default {
  components: { HeaderNavbar, TestContainer, Footer },
  name: 'Home',
}
</script>


<style>

.padTop{
  margin: 4rem 0 0 0
}

</style>