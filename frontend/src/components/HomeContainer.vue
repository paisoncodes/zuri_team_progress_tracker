<template>

<div class="my-6 pad-cont">

    <nav class="flex flex-col text-sm sm:flex-row">
        <button class="block py-4 font-medium bg-brand-red-light-1 padtab1 hover:text-blue-500 focus:outline-none text-brand-gray-dark-1 border-brand-gray-light">
            OVERVIEW 
        </button>
        
        <button class="block py-4 text-brand-gray-light padothers hover:text-brand-gray-dark-1 focus:outline-none">
            2021 <br> (10,000 interns)
        </button>
        
        <button class="block py-4 text-brand-gray-light padothers hover:text-brand-gray-dark-1 focus:outline-none">
            2020 <br> (10,000 interns)
        </button>
        
        <button class="block py-4 text-brand-gray-light padothers hover:text-brand-gray-dark-1 focus:outline-none">
            2019 <br> (10,000 interns)
        </button>
        <button class="block py-4 text-brand-gray-light padothers hover:text-brand-gray-dark-1 focus:outline-none">
            2018 <br> (10,000 interns)
        </button>
    </nav>

    <div class="bg-brand-red-light-1 ">
        <!-- 2021 -->
        <div class="flex">
            <div class="flex flex-col justify-center overview-width">
                <p>2021</p>
            </div>

            <div class="w-full">
                <OverallStats/>
                <CurrentJobPlacement/>
            </div>
        </div>

        <div class="flex">
            <div class="flex flex-col justify-center overview-width">
                <p>2020</p>
            </div>

            <div class="w-full">
                <OverallStats/>
                <CurrentJobPlacement/>
            </div>
        </div>

        <div class="flex">
            <div class="flex flex-col justify-center overview-width">
                <p>2019</p>
            </div>

            <div class="w-full">
                <OverallStats/>
                <CurrentJobPlacement class="mb-5"/>
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

.pad-cont{
    padding: 3rem;
    margin-top: 5rem;
}

.padtab1{
    padding: 0 1.07rem;
}

.padothers{
    padding: 1.2rem 2.41rem;
}

.overview-width {
    width: 7.2rem;
}
</style>