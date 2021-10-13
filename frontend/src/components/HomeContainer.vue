<template>
<div class="w-4/5 py-8 mx-auto">
    <div class="flex">
        <!-- This is the sidebar section -->
        <div class="w-1/5 p-2 bg-brand-red-light-2 text-brand-gray-dark-1 font-medium">
            <div class="">OVERVIEW</div>
            <div>2021</div>
        </div>
        <!-- This is the main section -->
        <div class="w-4/5 bg-brand-red-light-1">
            <!-- This is the navbar of the main section -->
            <div class="flex items-center justify-start py-2 px-8 space-x-20 bg-white text-brand-gray-light-1">
                <div class="hover:text-brand-gray-dark-1">
                    <router-link to="/">2021</router-link>
                </div>
                <div class="hover:text-brand-gray-dark-1">
                    <router-link to="/">2020</router-link>
                </div>
                <div class="hover:text-brand-gray-dark-1">
                    <router-link to="/">2019</router-link>
                </div>
                <div class="hover:text-brand-gray-dark-1">
                    <router-link to="/">2018</router-link>
                </div>
            </div>
            <!-- This is the main section   -->
            <div class="p-3 h-64 bg-brand-red-light-1"></div>
        </div>
    </div>
</div>
</template>

<script>
export default {

}
</script>

<style>

</style>