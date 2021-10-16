<template>

<div class="px-6 mx-auto max-w-7xl bg-brand-red-light-1">

    <div class="bg-brand-red-light-1" v-for="(this_year, i) in progresStat" :key="i">
        <div class="flex">
            <div class="flex overview-width flex-col justify-center w-32">
                <p>2020</p>
            </div>

            <div class="w-full">
                <Statistics 
                    :participants="this_year.participants" 
                    :femaleParticipants="this_year.female"
                    :maleParticipants="this_year.male" 
                />
                <CurrentJobPlacement 
                    :total_finalist="this_year.finalists" 
                    :total_employed="this_year.employed_finalists" 
                />
            </div>
        </div>

        <div class="flex">
            <div class="flex overview-width flex-col justify-center w-32">
                <p>2019</p>
            </div>

            <div class="w-full">
                <Stats19/>
                <CurrentJobPlacement/>
            </div>
        </div>

        <div class="flex">
            <div class="flex overview-width flex-col justify-center w-32">
                <p>2018</p>
            </div>

            <div class="w-full">
                <Stats18/>
                <CurrentJobPlacement class="mb-5"/>
            </div>
        </div>
        
    </div>

    
</div>
</template>

<script>
    import {mapGetters, mapActions } from 'vuex'
    import CurrentJobPlacement from '@/components/CurrentJobPlacement'
    import Statistics from '@/components/Statistics'

    export default {
        name: "HomeContainer",
        components:{
            CurrentJobPlacement,
            Statistics,
        },
        data(){
            return{}
        },
        methods: {
            ...mapActions(['getProgresStat']),

        },
        computed: {
            ...mapGetters(["progresStat"])
        },
        mounted() {
            this.getProgresStat()
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