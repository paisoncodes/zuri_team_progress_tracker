<template>

<div class="mx-auto my-6">

    <nav class="flex flex-col sm:flex-row">
        <button class="py-4 bg-brand-red-light-2 padtab1 block hover:text-blue-500 focus:outline-none text-brand-gray-dark-1 font-medium border-brand-gray-light">
            OVERVIEW
        </button>
        
        <button class="text-brand-gray-light py-4 padothers block hover:text-brand-gray-dark-1 focus:outline-none">
            2021
        </button>
        
        <button class="text-brand-gray-light py-4 padothers block hover:text-brand-gray-dark-1 focus:outline-none">
            2020
        </button>
        
        <button class="text-brand-gray-light py-4 padothers block hover:text-brand-gray-dark-1 focus:outline-none">
            2019
        </button>
        <button class="text-brand-gray-light py-4 padothers block hover:text-brand-gray-dark-1 focus:outline-none">
            2018
        </button>
    </nav>

    <div class="grid-cont">
        <div class="flex items-center bg-brand-red-light-2">
            <p class="mx-auto text-brand-gray-dark-1">2021</p>
        </div>

        <div>
            <div>
                <OverallStats/>
            </div>
                
            <div>
                <CurrentJobPlacement/>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import CurrentJobPlacement from '@/components/CurrentJobPlacement'
import OverallStats from '@/components/OverallStats'

export default {
name: "HomeContainer",
components:{
    CurrentJobPlacement,
    OverallStats
},
data(){
    return{

    }
}
}
</script>

<style scoped>

.padtab1{
    padding: 0 1.07rem;
}

.padothers{
    padding: 1.2rem 2.41rem;
}

.grid-cont {
    display: grid;
    grid-template-columns: 7.2rem 1fr;
    grid-template-rows: 1fr;
    grid-auto-flow: row;
}
</style>