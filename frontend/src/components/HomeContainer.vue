<template>

<div class="px-6 mx-auto max-w-7xl bg-brand-red-light-1">

    <div class="bg-brand-red-light-1">
        <div class="flex sm:flex-col">
            <div class="flex overview-width flex-col justify-center w-1/6">
                <p>2021</p>
            </div>

            <div class="w-full">
                <OverallStats/>
                <CurrentJobPlacement/>
            </div>
        </div>

        <div class="flex">
            <div class="flex overview-width flex-col justify-center w-1/6">
                <p>2020</p>
            </div>

            <div class="w-full">
                <OverallStats/>
                <CurrentJobPlacement/>
            </div>
        </div>

        <div class="flex">
            <div class="flex overview-width flex-col justify-center w-1/6">
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

.padtab1{
    padding: 0 1.07rem;
}

.padothers{
    padding: 1.2rem 2.41rem;
}


</style>