<template>
<div class="w-4/5 mx-auto">
    <!-- component -->
<div v-for="(profile, i) in profiles" :key="i" class="py-6 mx-auto ">
  <div class="flex mx-auto overflow-hidden shadow-md bg-brand-red-light-1 sm:max-w-xl md:max-w-full lg:max-w-screen-xl h-60">
    <div class="bg-cover w-96 h-60" style="background-image: url('./assets/mariam.png')">
    </div> 
    <div class="px-6 text-left">
      <h1 class="text-4xl font-normal font-bold leading-loose text-gray-900 text-brand-gray-dark-1">{{profile.name}}</h1>
      <h3 class="text-brand-gray-dark-1 leading-normal text-xl ">{{profile.role}}</h3>
      <h4 class="text-brand-gray-light leading-tight text-base py-4">{{profile.stage}}</h4>
      <p class="text-sm text-gray-600 text-brand-gray-light text-base ">{{profile.about}}</p>
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
           picture: require('../assets/mariam.png'),
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