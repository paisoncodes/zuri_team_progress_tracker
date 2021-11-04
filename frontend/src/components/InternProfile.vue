<template>
<div class="mx-auto max-w-7xl ">
  <!-- component -->
  <div v-for="profile in profiles.slice(6,7)" v-bind:key="profile.id" class="py-6 mx-auto">
    <div class="sm:grid grid-cols-3 lg:grid-cols-4 gap-6 mx-auto shadow-sm bg-brand-red-light-2">
    
      <img class="object-cover w-full h-96 rounded" v-bind:src="profile.picture" v-bind:alt="profile.alt" />
  
      <div class="grid-cols-2 sm:col-span-2 lg:col-span-3 py-4 text-left">
        <h1 class="text-2xl md:text-3xl font-medium text-brand-gray-dark-1">{{profile.full_name}}</h1>
        <h3 class="py-2 text-lg md:text-xl text-brand-gray-dark-1 ">{{profile.stack.join(',')}}</h3>
        <!-- <h4 class="py-2 text-brand-gray-light">{{profile.username}}</h4> -->
        <p class="text-brand-gray-light">{{profile.about}}</p>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
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
  }
}
</script>