<template>
<div class="mx-auto max-w-7xl ">
    <!-- component -->
<div v-for="profile in profiles.slice(6,7)" v-bind:key="profile.id" class="py-6 mx-auto">
  <div class="mx-auto shadow-xs md:overflow-hidden sm:flex bg-brand-red-light-2 md:h-full">
  
    <img class="object-cover w-full h-60 lg:w-60 rounded" v-bind:src="profile.picture" v-bind:alt="profile.alt" />
 
    <div class="px-6 py-4 text-left">
      <h1 class="text-4xl font-bold leading-loose text-brand-gray-dark-1">{{profile.full_name}}</h1>
      <h3 class="py-2 text-xl leading-normal text-brand-gray-dark-1 ">{{profile.stack.join(',')}}</h3>
      <h4 class="py-2 text-base leading-tight text-brand-gray-light">{{profile.username}}</h4>
      <p class="text-base text-brand-gray-light">{{profile.about}}</p>
    </div>
  </div>
</div>
</div>
</template>

<script>
import { mapGetters } from "vuex";
import { mapActions } from 'vuex'
export default {
  name: 'profiles',
    data(){
    return {

    }
  },
 computed: {
        ...mapGetters({
             profiles: 'internPictures'
        })
    },
    methods:{
    ...mapActions({
      interns: 'fetchInterns'
    })   
  },
  async created () {
    await this.interns()
      },  
}
</script>

<style>

</style>