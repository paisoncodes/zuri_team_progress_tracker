<template>
<div class="w-full min-h-pth bg-brand-red-light-1 ">
    <div class="flex justify-between items-center p-5 max-w-6xl mx-auto">

        <div class="text-base font-normal text-brand-gray-dark-1">ZURI.TEAM</div>

        <div class="hidden md:flex text-base space-x-5 items-center">
            <a href="#">Home</a>
            <a href="#">Curriculum</a>
            <a href="#">Program</a>
            <a href="#" class="text-brand-red-dark">Progress so far</a>
            <button class="bg-brand-red-dark hover:bg-white text-white hover:text-brand-red-dark font-normal px-4 py-4 text-sm">Join Zuri Training</button>
        </div>
        <!--mobile button-->
        <div class="md:hidden flex items-center">
           <button class="mobile-menu-button"><img src="../assets/hamburgerIcon.png" class="w-7 h-5" color="brand-gray-dark-1" v-on:click="menu()"></button>
        </div>

     </div>
     <!--mobile menu-->
        <div class="mobile-menu md:hidden  px-4">
            <a href="#" class=" block py-2 text-sm">Home</a>
            <a href="#" class=" block py-2 text-sm">Curriculum</a>
            <a href="#" class=" block py-2 text-sm">Program</a>
            <a href="#" class=" block py-2 text-sm text-brand-red-dark">Progress so far</a>
            <button class="bg-brand-red-dark hover:bg-white text-white hover:text-brand-red-dark font-normal py-4 text-sm w-full">Join Zuri Training</button>
        
        </div>
    <div class="font-normal py-12">
        <p class="text-brand-red-dark text-sm text-center py-6">INTERNS PROGRESS TRACKER</p>
        <h2 class="text-brand-gray-dark-1 lg:text-md text-center md:text-3xl sm:text-3xl mb-5">GET TO KNOW HOW WELL OUR INTERNS ARE DOING<br>
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