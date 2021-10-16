<template>
  <div class="mx-auto md:max-w-full lg:py-10 ">
    <div class="grid lg:grid-cols-4 md:grid-cols-2 md:gap-6">
    <div v-for="(intern, i) in interns" :key="i" class="w-full mx-auto overflow-hidden text-left transition-shadow duration-300 rounded-sm">
        <a href="/" aria-label=""><img class="object-cover w-full h-60" v-bind:src="intern.picture" v-bind:alt="intern.alt" /></a>
        <div  class="py-4">
         
          <a href="/" aria-label="" class="inline-block text-black transition-colors duration-200 hover:text-deep-purple-accent-700">
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