<template>
  <div>
    <form class="">
      <div class="block xs:flex justify-between items-center mb-4 xs:mb-10">
        <p style="color:red" v-if="this.$store.state.formOneConfirmation" class="text-center">Information saved</p>
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
          :src="item.imageUrl ? item.imageUrl : require('../assets/carbon_image.png')"
          alt="Uploaded image"
        />
        <input @change="upload" type="file" accept="image/*" id="image" />
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions, mapMutations } from "vuex";
import { mapFields } from "vuex-map-fields";

export default {
  data() {
    return {
      item: {
        image: null,
        imagesArray: null
      },
      imageUrl: null,
    };
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
    ...mapMutations(["setImageOne"]),
    
      async uploadImage(e) {
      let image = e.target.files[0];
      const reader = new FileReader();
      reader.readAsDataURL(image);
      var myimage = await callBack(g)

      var g = "mockVariable"
      this.imageUrl = myimage
      this.setImageOne(this.imageUrl)

      function callBack(g){
        console.log(g)
      return new Promise (function(resolve,reject){
        reader.onload = function(){
          resolve(reader.result);
        }
        reader.onerror = reject;
      })
      }

    }, 

    upload(e){
      let image = e.target.files[0];
      this.item.image = image;
      this.setImageOne(this.item.image)
    }
  

  },
};
</script>
