<template>
<div class="w-full p-5" >
    <h3 class="text-brand-gray-light font-normal"> CURRENT JOB PLACEMENTS </h3>
    <div>
        <!-- progress bar for total employed-->
        <div>
            <div class="flex justify-between text-brand-gray-light mt-4 font-normal">
                <p>January</p>
                <p>December</p>
            </div>

            <!-- main progress bar -->
            <div class="w-full bg-brand-red-light-3 rounded-full my-4">
                <div class="bg-brand-gray-dark-1 rounded-full h-3" :style="{width: progressWidth+'%'}" ></div>
            </div>

            <p class="text-brand-gray-light"> {{currentEmployed.toLocaleString()}} /  {{totalEmployed.toLocaleString()}} Employed</p>
      </div>
        
        <!-- Where some of our interns work -->
        <div class="my-8">
            <h3 class="text-brand-gray-light">WHERE SOME OF OUR</h3>
            <h3 class="text-brand-gray-light">INTERNS NOW WORK</h3>

            <div class="flex flex-wrap justify-between my-5">
                <img src="@/assets/CurrentJobPlacement/company_1.png">
                <img src="@/assets/CurrentJobPlacement/company_2.png">
                <img src="@/assets/CurrentJobPlacement/company_3.png">
                <img src="@/assets/CurrentJobPlacement/company_4.png">
                <img src="@/assets/CurrentJobPlacement/company_5.png">
                <img src="@/assets/CurrentJobPlacement/company_6.png">
                <img src="@/assets/CurrentJobPlacement/company_7.png">
                <img src="@/assets/CurrentJobPlacement/company_8.png">
            </div>
        </div>
        <div>
            <a href="#" class="text-blue-400">VIEW COMPLETE PROGRESS ></a>
        </div>
    </div>
</div>
</template>

<script>
export default {
    data(){
        return {
            progressWidth:0,
            currentEmployed:1545000,
            totalEmployed: 2056789
        }
    },
    methods:{
        employedPercentage(){
            let employPercent = (this.currentEmployed * 100) / this.totalEmployed
           return this.progressWidth = employPercent 
           
        },
    },
    mounted(){
        this.employedPercentage()
    }
}
</script>

<style>
    /* .test{
        width:94%
    } */
</style>