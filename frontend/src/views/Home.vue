<template>
  <div>
    <div class="bg-white text-center flex flex-col">
      <div v-show="this.$store.state.profileModalActive">
        <ProfileCard class="fixed" />
      </div>
      <HeaderNavComponent />
      <!--<Subscribe />-->
      <TabContainer class="padTop" />
      <LoginModal v-if="showLogin" />
    </div>
    <Footer />
  </div>
</template> 

<script>
import ProfileCard from "../components/ProfileCard.vue";
import HeaderNavComponent from "../components/HeaderNavComponent.vue";
// import Subscribe from "../components/Subscribe.vue";
import TabContainer from "../components/TabContainer.vue";
import Footer from "../components/Footer.vue";
import LoginModal from "@/components/LoginModal.vue";
export default {
  components: {
    ProfileCard,
    HeaderNavComponent,
    // Subscribe,
    TabContainer,
    LoginModal,
    Footer,
  },
  name: "Home",
  data() {
    return {
      displayCard: this.$store.state.profileModalActive,
      showLogin: false,
    };
  },
  mounted() {
    this.eventBus.on("toggleLoginModal", (data) => {
      this.showLogin = data;
    });
  },
};
</script>


<style>
.padTop {
  margin: 4rem 0 0 0;
}
</style>