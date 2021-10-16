<template>
<div class="mx-auto max-w-7xl ">
    <!-- component -->
<div v-for="(profile, i) in profiles" :key="i" class="py-6 mx-auto">
  <div class="mx-auto shadow-xs md:overflow-hidden sm:flex bg-brand-red-light-2 md:h-full">
  
    <img class="w-full md:h-full lg:w-60 " v-bind:src="profile.picture" v-bind:alt="profile.alt" />
 
    <div class="px-6 text-left">
      <h1 class="text-4xl font-bold leading-loose text-brand-gray-dark-1">{{profile.name}}</h1>
      <h3 class="py-2 text-xl leading-normal text-brand-gray-dark-1 ">{{profile.role}}</h3>
      <h4 class="py-2 text-base leading-tight text-brand-gray-light">{{profile.stage}}</h4>
      <p class="text-base text-brand-gray-light">{{profile.about}}</p>
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