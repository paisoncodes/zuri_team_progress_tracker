<template>
  <div class="max-w-6xl sm:max-w-xl md:max-w-full md:px-6 lg:py-6">
    <div class="grid grid-cols-4 gap-12 sm:max-w-sm sm:mx-auto lg:max-w-6xl">
    <div v-for="(intern, i) in interns" :key="i" class="text-left transition-shadow duration-300 rounded-sm ">
        <a href="/" aria-label="Article"><img class="object-cover w-64 h-60" v-bind:src="intern.picture" v-bind:alt="intern.alt" /></a>
        <div  class="py-4">
         
          <a href="/" aria-label="Article" class="inline-block text-black transition-colors duration-200 hover:text-deep-purple-accent-700">
            <p class="text-2xl font-bold leading-5 text-brand-gray-dark-1">
             {{ intern.name}}
            </p>
          </a>
          <p class="py-2 text-brand-gray-dark-1">
          {{intern.track}}
          </p>
          <div class="flex space-x-4">
            <span class="text-brand-gray-light">
         {{intern.stage}}
          </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: 'Interns',
  data(){
    return {
      interns:[
        {
          name:"Mariam Danjuma",
          track: 'UI/UX Designer/Figma',
          stage:  'Zuri Training Finalist',
           picture: require('../assets/mariam.png'),
           alt: 'Mariam Danjuma'
        },
        {
          name:"Felix Abasi Franklin",
          track: 'UI/UX Designer/Figma',
          stage:  'Zuri Training Finalist',
          picture: require('../assets/felix.png'),
          alt: 'Felix Abasi Franklin'
        },
        {
         name:"Afolanyan Gbeminiyi",
          track: 'UI/UX Designer/Figma',
          stage:  'Zuri Training Finalist',
          picture: require('../assets/afolayan.png'),
           alt: 'Afolanyan Gbeminiyi'
        },
        {
         name:"Namnso Ukpanah",
          track: 'UI/UX Designer/Figma',
          stage:  'Zuri Training Finalist',
          picture: require('../assets/namso.png'),
           alt: 'Namnso Ukpanah'
        },
      ]
    }
  },
  
}
</script>