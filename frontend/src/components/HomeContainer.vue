<template>

<div class="mt-0 max-w-6xl mx-auto container pad-cont">


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