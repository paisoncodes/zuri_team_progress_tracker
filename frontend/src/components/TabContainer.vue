<template>
    <div>

        <div class="pt-0">

            <nav class="flex flex-row items-center mx-auto overflow-y-auto text-sm md:flex-row max-w-7xl">  
                <ul class="flex">  
                    <li @click="component = 'HomeContainer', activeTab = 1" class="block py-6 cursor-pointer bg-brand-red-light focus:outline-none text-brand-gray-dark-1 border-brand-gray-light w-36 " :class="{'is-active': activeTab === 1}">          
                        OVERVIEW
                    </li>  
                    <li @click="component = 'TwentyOne', activeTab = 2; changeYear(2021)"  class="block py-4 cursor-pointer text-brand-gray-light w-36 hover:text-brand-gray-dark-1 focus:outline-none" :class="{'is-active': activeTab === 2}">                      
                        2021 <br> ({{filteredIndex[3]}} interns)        
                    </li>
                    <li @click="component = 'Twenty', activeTab = 3; changeYear(2020)" class="block py-4 cursor-pointer text-brand-gray-light w-36 hover:text-brand-gray-dark-1 focus:outline-none" :class="{'is-active': activeTab === 3}">                  
                        2020 <br> ({{filteredIndex[2]}}  interns)        
                    </li>
                    <li @click="component = 'Nineteen', activeTab = 4; changeYear(2019)" class="block py-4 cursor-pointer text-brand-gray-light w-36 hover:text-brand-gray-dark-1 focus:outline-none" :class="{'is-active': activeTab === 4}">                    
                        2019 <br> ({{filteredIndex[1]}}  interns)        
                    </li>
                    <li @click="component = 'Eighteen', activeTab = 5; changeYear(2018)" class="block py-4 cursor-pointer text-brand-gray-light w-36 hover:text-brand-gray-dark-1 focus:outline-none" :class="{'is-active': activeTab === 5}">                        
                        2018 <br> ({{filteredIndex[0]}}  interns)        
                    </li>  
                </ul>        
            </nav>

            <component :is="component"> </component>
        
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import HomeContainer from '@/components/HomeContainer.vue'
import Eighteen from '@/components/Eighteen.vue'
import Nineteen from '@/components/Nineteen.vue'
import Twenty from '@/components/Twenty.vue'
import TwentyOne from '@/components/TwentyOne.vue'
import { mapActions } from 'vuex'
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
            activeTab: 1,
            statIndex:[],
            filteredIndex: [],
        }
    },
    methods: {
        ...mapActions([
            'getStackYear',
            'getYear'
        ]),
        changeYear(year) {
            this.getStackYear(year)
            this.getYear(year)
        }
    },
    created(){
        axios.get('https://zuri-progress-tracker.herokuapp.com/api/v1/statistics/')
        .then(
            res=> this.statIndex = res.data.slice(2)
            )
    },
    computed:{
        filterYear(){
            this.statIndex.forEach(item => {
                this.filteredIndex.push(item.year)
            });
        }
    }
}
</script>

<style>

.is-active {
    background-color: #F7F3F2;
}

.button-width{
    width: 15.5%;
}

</style>