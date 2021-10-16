<template>
  <div class="text-left">
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
          <form class="m-8" @submit.prevent="toggleModal()">
            <!-- CONTENT -->
            <div class="sm:text-left">
              <h1 class="mb-6 text-2xl text-gray-dark-1">LOGIN</h1>
              <p class="mb-3 text-sm text-gray-dark-1">PASSWORD</p>
              <input
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
export default {
  methods: {
    showLogin() {
      this.eventBus.emit("toggleLoginModal", false);
    },
    toggleModal() {
      this.showLogin()
      this.$store.commit('toggleProfileEditModal');
    },
  },
};
</script>

<style></style>
