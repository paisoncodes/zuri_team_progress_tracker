<template>
    <div>

        <div class="pt-0">

            <nav class="flex flex-row items-center mx-auto overflow-y-auto text-sm md:flex-row max-w-7xl">  
                <ul class="flex">  
                    <li @click="component = 'HomeContainer', activeTab = 1" class="block py-6 cursor-pointer bg-brand-red-light focus:outline-none text-brand-gray-dark-1 border-brand-gray-light w-36 " :class="{'is-active': activeTab === 1}">          
                        OVERVIEW
                    </li>  
                    <li @click="component = 'TwentyOne', activeTab = 2"  class="block py-4 cursor-pointer text-brand-gray-light w-36 hover:text-brand-gray-dark-1 focus:outline-none" :class="{'is-active': activeTab === 2}">                      
                        2021 <br> (10,000 interns)        
                    </li>
                    <li @click="component = 'Twenty', activeTab = 3" class="block py-4 cursor-pointer text-brand-gray-light w-36 hover:text-brand-gray-dark-1 focus:outline-none" :class="{'is-active': activeTab === 3}">                  
                        2020 <br> ({{ stats20.participants }} interns)        
                    </li>
                    <li @click="component = 'Nineteen', activeTab = 4" class="block py-4 cursor-pointer text-brand-gray-light w-36 hover:text-brand-gray-dark-1 focus:outline-none" :class="{'is-active': activeTab === 4}">                    
                        2019 <br> ({{ stats19.participants }} interns)        
                    </li>
                    <li @click="component = 'Eighteen', activeTab = 5" class="block py-4 cursor-pointer text-brand-gray-light w-36 hover:text-brand-gray-dark-1 focus:outline-none" :class="{'is-active': activeTab === 5}">                        
                        2018 <br> ({{ stats.participants }} interns)        
                    </li>  
                </ul>        
            </nav>

            <component :is="component"> </component>
        
        </div>
    </div>
</template>


<script>
import { mapActions } from 'vuex'
import HomeContainer from '@/components/HomeContainer.vue'
import Eighteen from '@/components/Eighteen.vue'
import Nineteen from '@/components/Nineteen.vue'
import Twenty from '@/components/Twenty.vue'
import TwentyOne from '@/components/TwentyOne.vue'

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
            activeTab: 1
        }
    },
    computed: {
        stats() {
            return this.$store.state.stats18
        },
        stats19(){
            return this.$store.state.stats19
        },
        stats20(){
            return this.$store.state.stats20
        }

    },
    methods: {
        ...mapActions(['getStatistics18, getStatistics19, getStatistics20']),

    },
    async created() {
        this.getStatistics18('2018')
        this.getStatistics18('2019')
        this.getStatistics18('2020')
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