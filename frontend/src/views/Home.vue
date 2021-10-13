<template>
  <div class="text-center">
    <div class="bg-brand-gray-light-2">This is the official page of the project tracker app</div> 
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
