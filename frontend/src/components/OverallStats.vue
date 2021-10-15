<template>
    <div class="mr-5 mt-5">
        <div class="md:py-4 bg-brand-red-light-2 text-center md:text-center flex flex-col md:flex-col lg:flex-row md:justify-self auto">

            <div v-for="stat in stats" :key="stat.category" class="py-11 md:py-0 md:px-11 border-b-2 md:border-b-0 md:border-r-2 border-brand-red-light-3 ">
                
                <div class="py-3 text-xs">
                    <h1 class="text-brand-gray-light">TOTAL NUMBER</h1>
                    <h1 class="text-brand-gray-light ">{{ stat.category }}</h1>
                </div>
                
                <h1 class="text-brand-gray-dark-1 text-3xl">{{ stat.figure }}</h1>
            </div>

            <div class="py-11 md:py-0 md:px-11 border-brand-red-light-3 flex-grow text-sm">
                <div class="pt-3 text-xs">
                    <h1 class="text-brand-gray-light ">PARTICIPANT</h1>
                    <h1 class="text-brand-gray-light">LOCATIONS</h1>
                </div>
                <h1 class="text-brand-gray-dark-1 text-xs mt-3">Lagos <br> Kaduna <br> And from around the world </h1>
            </div>   

        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            stats: [
                {category: 'OF PARTICIPANTS', figure: '2,056,789'},
                {category: 'OF FEMALE PARTICIPANTS', figure: '1,578,789'},
                {category: 'OF MALE PARTICIPANTS', figure: '900,789'}
            ]
        }
    }
}
</script>

<style scoped>

.test{
    width: 100%;
}

</style>