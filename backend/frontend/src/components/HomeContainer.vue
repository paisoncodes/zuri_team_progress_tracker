<template>

<div class="mx-auto max-w-7xl bg-brand-red-light-1">

    <div class="w-full h-auto bg-brand-red-light-1" v-for="(this_year, i) in progresStat" :key="i">
        <div class="flex">
            <div class="bor h-auto bg-brand-red-light-2 flex overview-width flex-col justify-center w-44">
                <p>{{this_year.year}}</p>
                <div class="w-44">
                    <img class="inline-block align-middle mx-1 my-5" v-for="intern in sponsors" v-bind:key="intern.id" v-bind:src="intern.pic">
                </div>
            </div>

            <div class="w-full">
                <Statistics 
                    :participants="this_year.participants" 
                    :femaleParticipants="this_year.female"
                    :maleParticipants="this_year.male" 
                />
                <CurrentJobPlacement class="mb-6"
                    :total_finalist="this_year.finalists" 
                    :total_employed="this_year.employed_finalists" 
                />
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
            return{
                sponsors: [
                    {id: 1, pic: require("@/assets/hng.png")},
                    {id: 2, pic: require("@/assets/ss.jpeg")},
                    {id: 3, pic: require("@/assets/flutterwave.png")},
                    {id: 4, pic: require("@/assets/paystack.png")},
                    {id: 5, pic: require("@/assets/paypal.png")},
                    {id: 6, pic: require("@/assets/clubhouse.png")},
                ]
            }
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

img{
    width: 48px;
    height: 48px;
    border-radius: 50%;
}

.bor{
    margin-bottom: 24.2px;
    margin-top: 20px;
}




</style>