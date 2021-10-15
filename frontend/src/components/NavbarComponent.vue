<template>
<div class="w-full min-h-pth bg-brand-red-light-1 ">
    <div class="flex items-center justify-between max-w-6xl p-5 mx-auto">

        <div class="text-base font-normal text-brand-gray-dark-1">ZURI.TEAM</div>

        <div class="items-center hidden space-x-5 text-base md:flex">
            <a href="#" class="">Home</a>
            <a href="#" class="">Curriculum</a>
            <a href="#" class="">Program</a>
            <a href="#" class=" text-brand-red-dark">Progress so far</a>
            <button class="px-4 py-4 text-sm font-normal text-white bg-brand-red-dark hover:bg-white hover:text-brand-red-dark">Join Zuri Training</button>
        </div>
        <!--mobile button-->
        <div class="flex items-center md:hidden">
           <button class="mobile-menu-button"><img src="../assets/hamburgerIcon.png" class="h-5 w-7" color="brand-gray-dark-1" v-on:click="menu()"></button>
        </div>

     </div>
     <!--mobile menu-->
        <div class="px-4 mobile-menu md:hidden">
            <a href="#" class="block py-2 text-sm ">Home</a>
            <a href="#" class="block py-2 text-sm ">Curriculum</a>
            <a href="#" class="block py-2 text-sm ">Program</a>
            <a href="#" class="block py-2 text-sm text-brand-red-dark">Progress so far</a>
            <button class="w-full py-4 text-sm font-normal text-white bg-brand-red-dark hover:bg-white hover:text-brand-red-dark">Join Zuri Training</button>
        
        </div>
    <div class="py-12 font-normal">
        <p class="py-6 text-sm text-center text-brand-red-dark">INTERNS PROGRESS TRACKER</p>
        <h2 class="mb-5 text-center text-brand-gray-dark-1 lg:text-md md:text-3xl sm:text-3xl">GET TO KNOW HOW WELL OUR INTERNS ARE DOING<br>
            AND WHERE THEY CURRENTLY ARE</h2>
    </div>
   
</div>
</template>

<script>
export default {
    data(){
        },
        methods:{
            menu(){
                const menu = document.querySelector('.mobile-menu' )
                menu.classList.toggle("hidden");  

        },
   }
}
</script>

<style>

</style>