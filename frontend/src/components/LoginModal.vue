<template>
  <div class="text-left">
    <div class="relative">
  <div v-show="this.$store.state.profileModalActive" class="absolute">
        <ProfileCard/>
      </div>
      </div>
    <div
      class="fixed z-10 inset-0 overflow-y-auto"
      aria-labelledby="modal-title"
      role="dialog"
      aria-modal="true"
    >
      <div
        class="
          flex
          items-end
          justify-center
          min-h-screen
          pt-4
          px-4
          pb-20
          text-center
          sm:block
          sm:p-0
        "
      >
        <div
          class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
          aria-hidden="true"
        ></div>

        <!-- This element is to trick the browser into centering the modal contents. -->
        <span
          class="hidden sm:inline-block sm:align-middle sm:h-screen"
          aria-hidden="true"
          >&#8203;</span
        >

        <div
          class="
            inline-block
            align-bottom
            bg-white
            text-left
            overflow-hidden
            shadow-xl
            transform
            transition-all
            sm:my-8
            sm:align-middle
            sm:max-w-lg
            sm:w-full
          "
        >
          <div @click="showLogin" class="float-right pt-8 pr-8 cursor-pointer">
            <i
              class="fa fa-times text-gray-dark-1 hover:text-brand-gray-light"
              aria-hidden="true"
            ></i>
          </div>
          <form class="m-8" @submit.prevent="login()">
            <!-- CONTENT -->
            <div class="sm:text-left">
              <h1 class="mb-6 text-2xl text-gray-dark-1">LOGIN</h1>
              <div class="flex items-center mb-3">
              <p class=" text-sm text-gray-dark-1 mr-3">PASSWORD</p>
               <!-- <div  @click="this.showAlert = false;" >
                 <i  class="fa fa-times"  aria-hidden="true" ></i>
            </div> -->
               <div class="w-full bg-red-100 border border-red-400 text-red-700  relative" v-if="showAlert" role="alert">
                  <span class="m-4">Invalid Password</span>
                  <div  @click="showAlert = false;" class="absolute  bottom-0 right-2 top-1 cursor-pointer  text-red-500 hover:text-brand-gray-light">
                 <i class="fa fa-times" aria-hidden="true" ></i>
            </div>
                </div>
              </div>
              <input
                required
                v-model="password"
                type="text"
                name=""
                id=""
                placeholder="Enter your password here"
                class="w-full px-2 py-2 text-left outline-black"
              />
            </div>

            <!-- FOOTER -->
            <div class="mb-8 mt-5 sm:flex sm:flex-row-reverse">
              
              <button
              type="submit"
                class="
                  px-8
                  py-2
                  ml-4
                  text-white
                  border
                  border-brand-gray-dark-1
                  bg-brand-gray-dark-1
                  hover:bg-brand-gray-light
                  hover:text-white
                "
              >
                Login
              </button>
              <button
                @click="showLogin"
                class="
                  px-8
                  py-2
                  ml-4
                  text-white
                  border
                  text-brand-gray-dark-1
                  border-brand-gray-dark-2
                  hover:bg-brand-gray-light
                  hover:text-white
                "
              >
                Cancel
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProfileCard from '../components/ProfileCard.vue'
export default {
  data(){
    return{
      password:'',
      showAlert:false
    }
  },
  methods: {
    showLogin() {
      this.eventBus.emit("toggleLoginModal", false);
    },
    toggleModal() {
      // this.showLogin()
      this.eventBus.emit("toggleLoginModal", false); 
      this.$store.commit('toggleProfileEditModal')
    },
    login(){
      
      if(this.password == 'admin'){
        this.toggleModal()
      }else{
        this.showAlert = true;
        this.closeAlert()
      }
    },
    closeAlert(){
  
    setTimeout(function(){
      this.showAlert = false;
    }, 3000);
    }
  },
  components:{
    ProfileCard
  }
};
</script>

<style></style>
