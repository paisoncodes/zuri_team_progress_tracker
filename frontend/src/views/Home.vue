<template>
  <div>
    <div class="bg-white text-center flex flex-col">
      <NavbarComponent/>
      <Subscribe/>
      <TestContainer class="padTop"/>
    </div>
    <Footer />
  </div>
</template>

<script>
import NavbarComponent from '../components/NavbarComponent.vue'
import Subscribe from "../components/Subscribe.vue"
import TestContainer from '../components/TabContainer.vue'
import Footer from '../components/Footer.vue'

export default {
  components: { NavbarComponent, Subscribe, TestContainer, Footer },
  name: 'Home',
}
</script>


<style>

.padTop{
  margin: 4rem 0 0 0
}

</style>