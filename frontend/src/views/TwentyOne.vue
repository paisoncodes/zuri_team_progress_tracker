<template>
  <div class="bg-white text-center flex flex-col">
    <NavbarComponent/>
    <Subscribe/>
    <TwentyOneContainer/>

  </div>
</template>

<script>
import NavbarComponent from '../components/NavbarComponent.vue'
import Subscribe from '../components/Subscribe.vue'
import TwentyOneContainer from '../components/TwentyOneContainer.vue'

export default {
  components: { NavbarComponent, Subscribe, TwentyOneContainer},
  name: 'TwentyOne',
}
</script>