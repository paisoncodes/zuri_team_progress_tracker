<template>
    <div class="mt-5">
        <div class="md:py-4 bg-brand-red-light-2 text-center md:text-center flex flex-col md:flex-col lg:flex-row md:justify-self auto">

            <div class="py-11 md:py-0 md:px-11 border-b-2 md:border-b-0 md:border-r-2 border-brand-red-light-3 ">
                
                <div class="py-3 text-xs md:text-left sm:text-center">
                    <h1 class="text-brand-gray-light">TOTAL NUMBER <br>OF PARTICIPANTS</h1>
                </div>
                <h1 class="text-brand-gray-dark-1 md:text-left sm:text-center text-3xl">{{ stats.participants }}</h1>
            </div>
            <div class="py-11 md:py-0 md:px-11 border-b-2 md:border-b-0 md:border-r-2 border-brand-red-light-3 ">
                <div class="py-3 text-xs md:text-left sm:text-center">
                    <h1 class="text-brand-gray-light">TOTAL NUMBER <br>OF FEMALE PARTICIPANTS </h1>
                </div>
                <h1 class="text-brand-gray-dark-1 md:text-left sm:text-center text-3xl">{{ stats.female }}</h1>
            </div>

            <div class="py-11 md:py-0 md:px-11 border-b-2 md:border-b-0 md:border-r-2 border-brand-red-light-3 ">
                <div class="py-3 text-xs md:text-left sm:text-center">
                    <h1 class="text-brand-gray-light">TOTAL NUMBER <br>OF MALE PARTICIPANTS</h1>
                </div>
                <h1 class="text-brand-gray-dark-1 md:text-left sm:text-center text-3xl">{{ stats.male }}</h1>
            </div>

            <div class="py-11 md:py-0 md:px-11 border-brand-red-light-3 flex-grow text-sm">
                <div class="pt-3 text-xs md:text-left sm:text-center">
                    <h1 class="text-brand-gray-light ">PARTICIPANTS <br>LOCATIONS</h1>
                </div>
                <h1 class="text-brand-gray-dark-1 text-xs mt-3 md:text-left sm:text-center">Lagos <br> Kaduna <br> And from around the world </h1>
            </div>   

        </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
    computed: {
        stats() {
            return this.$store.state.stats19
        }
    },
    methods: {
        ...mapActions(['getStatistics19']),

    },
    async created() {
        this.getStatistics19('2019')
    }
}
</script>

<style scoped>

</style>