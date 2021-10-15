<template>
<div class="max-w-6xl mx-auto">
    <!-- component -->
<div v-for="(profile, i) in profiles" :key="i" class="py-16 mx-auto">
  <div class="flex mx-auto shadow-sm max-w-7xl bg-brand-red-light-2 ">
    <div class="bg-cover w-96 h-60">
    <img class="object-cover w-64 h-60" v-bind:src="profile.picture" v-bind:alt="profile.alt" />
    </div> 
    <div class="mx-4 text-left">
      <h1 class="text-4xl font-bold leading-loose text-brand-gray-dark-1">{{profile.name}}</h1>
      <h3 class="text-xl leading-normal text-brand-gray-dark-1 ">{{profile.role}}</h3>
      <h4 class="py-4 text-base leading-tight text-brand-gray-light">{{profile.stage}}</h4>
      <p class="text-base text-brand-gray-light ">{{profile.about}}</p>
    </div>
  </div>
</div>
</div>
</template>

<script>
export default {
  name: 'profiles',
  data(){
    return {
      profiles:[
        {
          name:"John Doe",
          role: 'Senior Digital Product Designer @andela',
          stage:  'Zuri Training Finalist',
           picture: require('../assets/chuks.png'),
           alt: 'Mariam Danjuma',
           about: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Accumsan sit amet in morbi dolor nunc, at. At scelerisque sed leo in pharetra. Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
        },
        
      ]
    }
  },
  
}
</script>

<style>

</style>