<template>
  <div>
    <div class="bg-white text-center flex flex-col">
      <div v-show="this.$store.state.profileModalActive">
        <ProfileCard class="fixed"/>
      </div>
      <NavbarComponent/>
      <Subscribe/>
      <TabContainer class="padTop"/>
    </div>
    <Footer />
  </div>
</template>

<script>
import ProfileCard from '../components/ProfileCard.vue'
import NavbarComponent from '../components/NavbarComponent.vue'
import Subscribe from "../components/Subscribe.vue"
import TabContainer from '../components/TabContainer.vue'
import Footer from '../components/Footer.vue'

export default {
  components: { ProfileCard, NavbarComponent, Subscribe, TabContainer, Footer },
  name: 'Home',
  data(){
    return{
            displayCard: this.$store.state.profileModalActive
    }
  }
}
</script>


<style>

.padTop{
  margin: 4rem 0 0 0
}

</style>