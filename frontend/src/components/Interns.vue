<template>
  <div class="mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:py-20">
    <div class="grid gap-2 lg:grid-cols-4 sm:max-w-sm sm:mx-auto lg:max-w-full">
    <div v-for="(intern, i) in interns" :key="i" class="overflow-hidden text-left transition-shadow duration-300 rounded-sm">
        <a href="/" aria-label="Article"><img class="object-cover w-64 h-60" v-bind:src="intern.picture" v-bind:alt="intern.alt" /></a>
        <div  class="py-4">
         
          <a href="/" aria-label="Article" class="inline-block text-black transition-colors duration-200 hover:text-deep-purple-accent-700">
            <p class="text-2xl font-bold leading-5 text-brand-gray-dark-1">
             {{ intern.name}}
            </p>
          </a>
          <p class="py-2 text-gray-700 text-brand-gray-dark-1">
          {{intern.track}}
          </p>
          <div class="flex space-x-4">
            <span class="text-gray-700 text-brand-gray-light">
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