<template>
    <div>

        <div class="pt-0">

        <nav class="flex flex-col text-sm sm:flex-row mx-auto px-6 max-w-7xl">      
            <button @click="component = 'HomeContainer'" class="block py-4 text-brand-gray-light-1 w-36 hover:text-brand-gray-dark-1 focus:outline-none">							
                OVERVIEW 
            </button>  

            <button @click="component = 'TwentyOne'" class="block py-4 font-medium bg-brand-red-light hover:text-blue-500 focus:outline-none text-brand-gray-dark-1 border-brand-gray-light bg-brand-red-light-1 w-36">						
                2021 <br> (10,000 interns)        
            </button>

            <button @click="component = 'Twenty'" class="block py-4 text-brand-gray-light w-36 hover:text-brand-gray-dark-1 focus:outline-none">					
                2020 <br> (10,000 interns)        
            </button>

            <button @click="component = 'Nineteen'" class="block py-4 text-brand-gray-light w-36 hover:text-brand-gray-dark-1 focus:outline-none">					
                2019 <br> (10,000 interns)         
            </button>

            <button @click="component = 'Eighteen'" class="block py-4 text-brand-gray-light w-36 hover:text-brand-gray-dark-1 focus:outline-none">						
                2018 <br> (10,000 interns)        
                        </button>          
        </nav>

            <component :is="component"> </component>
        
        </div>
    </div>
</template>


<script>
import HomeContainer from './HomeContainer.vue'
import Eighteen from './Eighteen.vue'
import Nineteen from './Nineteen.vue'
import Twenty from './Twenty.vue'
import TwentyOne from './TwentyOne.vue'

export default {
    components: {
        Eighteen,
        Nineteen,
        Twenty,
        TwentyOne,
        HomeContainer
    },
    data(){
        return{
            component: 'HomeContainer',
            showClass: false
        }
    }
}
</script>

<style>



</style>