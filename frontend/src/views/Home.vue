<template>
  <div class="bg-red-100 ">
    <p class="text-center">This is the official page of the project tracker app</p>
    <HomeContainer />
  </div>
</template>

<script>
import HomeContainer from '../components/HomeContainer.vue'

export default {
  components: { HomeContainer },
  name: 'Home',
}
</script>
