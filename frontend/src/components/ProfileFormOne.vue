<template>
  <div>
    <form class="">
      <div class="block xs:flex justify-between items-center mb-4 xs:mb-10">
        <h1 class="text-2xl">SOJI AMINU'S PROFILE</h1>
        <p class="text-2xl text-brand-gray-light">1/2</p>
      </div>

      <div class="w-full mb-3 sm:mb-5 sm:mr-12">
        <label class="">EDIT NAME</label><br />
        <input
          type="text"
          v-model="full_name"
          placeholder="Enter your name"
          class="
            w-full
            text-brand-gray-light
            p-2
            mt-1
            sm:mt-3
            border
            focus:outline-none
            border-black
          "
        />
      </div>
      <div class="w-full mb-3 sm:mb-5">
        <label class="">EDIT SALARY</label><br />
        <input
          type="text"
          v-model="currentSalary"
          placeholder="Enter your current salary here"
          class="
            w-full
            text-brand-gray-light
            p-2
            mt-1
            sm:mt-3
            border
            focus:outline-none
            border-black
          "
        />
        <p class="text-brand-gray-light mt-1.5">
          Note: Salary details will be kept private
        </p>
      </div>
      <div class="w-full mb-1 sm:mr-12">
        <label class="">EDIT ABOUT</label><br />
        <textarea
          v-model="about"
          placeholder="Express things about you"
          class="
            w-full
            h-24
            resize-none
            text-brand-gray-light
            p-2
            mt-1
            sm:mt-3
            border border-black
            focus:outline-none
          "
        ></textarea>
      </div>
      <div class="mb-4">
        <label>Currently Employed</label>
        <input class="ml-2" type="checkbox" v-model="employed" />
      </div>
      <div>
        <label>UPDATE PICTURE</label>
        <img
          class="w-16 h-16 cursor-pointer"
          src="../assets/carbon_image.png"
          alt=""
        />
        <input type="file" name="image" id="image" />
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions, mapMutations } from "vuex";
import { mapFields } from "vuex-map-fields";

export default {
  data() {
    return {};
  },
  computed: {
    ...mapFields([
      "formOne.full_name",
      "formOne.currentSalary",
      "formOne.about",
      "formOne.employed",
    ]),
  },
  methods: {
    ...mapActions(["editIntern"]),
    ...mapMutations(["setData"]),
  },
};
</script>
