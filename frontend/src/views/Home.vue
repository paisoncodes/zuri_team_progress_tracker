<template>
  <div class="">
   
    <!-- <HomeContainer /> -->
    <InternProfile />
    <Interns />
  </div>
</template>

<script>
// import HomeContainer from '../components/HomeContainer.vue'
import InternProfile from '../components/InternProfile.vue'
import Interns from '../components/Interns.vue'

export default {
  components: {  InternProfile, Interns },
  name: 'Home',
}
</script>
