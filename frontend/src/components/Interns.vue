<template>
  <div class="mx-auto md:max-w-full lg:py-10 ">
    <div class="grid lg:grid-cols-4 md:grid-cols-2 md:gap-6">
    <div v-for="intern in interns" v-bind:key="intern.id"  class="w-full mx-auto overflow-hidden text-left transition-shadow duration-300 rounded-sm">
        <a href="/" aria-label=""><img class="object-cover w-full h-60" v-bind:src="intern.picture" v-bind:alt="intern.alt" /></a>
        <div  class="py-4">
         
          <a href="/" aria-label="" class="inline-block text-black transition-colors duration-200 hover:text-deep-purple-accent-700">
            <p class="text-2xl font-bold leading-5 text-brand-gray-dark-1">
             {{ intern.full_name}}
            </p>
          </a>
          <p class="py-2 text-brand-gray-dark-1">
          {{intern.stack}}
          </p>
          <div class="flex space-x-4">
            <span class="text-brand-gray-light">
         Zuri Training Finalist
          </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>

import axios from "axios"

export default {
  name: 'Interns',
  data(){
    return {
      interns:[],
  }
  },
   created () {
    axios
     .get ('https://zuri-progress-tracker.herokuapp.com/api/v1/interns/')
      .then(res => {
        this.interns = res.data.slice(0,12);
      })
         
        .catch(error => {
          console.log(error.response)
        })
      }
  
}
</script>