<template>
  <div>
    <div class="bg-white text-center flex flex-col">
      <NavbarComponent/>
      <Subscribe/>
      <TestContainer class="padTop"/>
        <LoginModal v-if="showLogin"/>
    </div>
    <Footer />
  </div>
</template>

<script>
import NavbarComponent from '../components/NavbarComponent.vue'
import Subscribe from "../components/Subscribe.vue"
import TestContainer from '../components/TabContainer.vue'
import Footer from '../components/Footer.vue'
import LoginModal from '@/components/LoginModal.vue'
export default {
  
  data(){
    return{
      showLogin:false
    }
  },
  components: { NavbarComponent, Subscribe, TestContainer, LoginModal, Footer },
  name: 'Home',
  
    mounted (){
    this.eventBus.on('toggleLoginModal', (data) => {
      this.showLogin = data;
    })
  }
}
</script>


<style>

.padTop{
  margin: 4rem 0 0 0
}

</style>