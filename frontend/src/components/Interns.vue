<template>
  <div class="mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:py-20">
    <div class="grid gap-2 lg:grid-cols-4 sm:max-w-sm sm:mx-auto lg:max-w-full">
    <div v-for="(intern, i) in interns" :key="i" class="overflow-hidden text-left transition-shadow duration-300 rounded-sm">
        <a href="/" aria-label="Article"><img src="https://images.pexels.com/photos/2123755/pexels-photo-2123755.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=2&amp;h=750&amp;w=1260" class="object-cover w-64 h-60 " alt="" /></a>
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
  name: 'VotersTable',
  data(){
    return {
      interns:[
        {
          name:"John Doe",
          track: 'UI/UX Designer/Figma',
          stage:  'Zuri Training Finalist',
        
        },
        {
          name:"John Doe",
          track: 'UI/UX Designer/Figma',
          stage:  'Zuri Training Finalist',
         
        },
        {
         name:"John Doe",
          track: 'UI/UX Designer/Figma',
          stage:  'Zuri Training Finalist',
        },
        {
         name:"John Doe",
          track: 'UI/UX Designer/Figma',
          stage:  'Zuri Training Finalist',
        },
      ]
    }
  },
  
}
</script>