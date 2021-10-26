<template>
    <div>

        <div class="pt-0">

            <nav class="flex flex-row items-center mx-auto overflow-y-auto text-sm md:flex-row max-w-7xl">  
                <ul class="flex">  
                    <li @click="component = 'HomeContainer', activeTab = 1" class="block py-6 cursor-pointer bg-brand-red-light focus:outline-none text-brand-gray-dark-1 border-brand-gray-light w-44 " :class="{'is-active': activeTab === 1}">          
                        OVERVIEW
                    </li>  
                    <li @click="component = 'TwentyOne', activeTab = 2; changeYear(2021)"  class="block py-4 cursor-pointer text-brand-gray-light w-44 hover:text-brand-gray-dark-1 focus:outline-none" :class="{'is-active': activeTab === 2}">                      
                        2021 <br> ({{yearParticipants[0]}} interns)        
                    </li>
                    <!-- <li @click="component = 'Twenty', activeTab = 3; changeYear(2020)" class="block py-4 cursor-pointer text-brand-gray-light w-44 hover:text-brand-gray-dark-1 focus:outline-none" :class="{'is-active': activeTab === 3}">                  
                        2020 <br> ({{yearParticipants[1]}}  interns)        
                    </li>
                    <li @click="component = 'Nineteen', activeTab = 4; changeYear(2019)" class="block py-4 cursor-pointer text-brand-gray-light w-44 hover:text-brand-gray-dark-1 focus:outline-none" :class="{'is-active': activeTab === 4}">                    
                        2019 <br> ({{yearParticipants[2]}}  interns)        
                    </li>
                    <li @click="component = 'Eighteen', activeTab = 5; changeYear(2018)" class="block py-4 cursor-pointer text-brand-gray-light w-44 hover:text-brand-gray-dark-1 focus:outline-none" :class="{'is-active': activeTab === 5}">                        
                        2018 <br> ({{yearParticipants[3]}}  interns)        
                    </li>   -->
                </ul>        
            </nav>

            <component :is="component"> </component>
        
        </div>
    </div>
</template>


<script>
import HomeContainer from '@/components/HomeContainer.vue'
import Eighteen from '@/components/Eighteen.vue'
import Nineteen from '@/components/Nineteen.vue'
import Twenty from '@/components/Twenty.vue'
import TwentyOne from '@/components/TwentyOne.vue'
import { mapActions, mapGetters } from 'vuex'
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
    computed:{
        ...mapGetters(["yearParticipants"])
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