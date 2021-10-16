<template>
<div class="w-full min-h-pth bg-brand-red-light-1 py-2">
    <div class="flex justify-between items-center py-14 max-w-6xl mx-auto px-5">

        <div class="text-base font-normal text-brand-gray-dark-1 font-mulish">ZURI.TEAM</div>

        <div class="hidden md:flex text-base space-x-5 items-center font-mulish">
            <a href="#">Home</a>
            <a href="#">Curriculum</a>
            <a href="#">Program</a>
            <a href="#" class="text-brand-red-dark">Progress so far</a>
            <button class="bg-brand-red-dark hover:bg-white text-white hover:text-brand-red-dark font-normal px-6 py-2 text-sm">Join Zuri Training</button>
        </div>
        <!--mobile button-->
        <div class="md:hidden flex items-center">
           <button class="mobile-menu-button"><img src="../assets/hamburgerIcon.png" class="w-7 h-5" color="brand-gray-dark-1" v-on:click="menu()"></button>
        </div>

     </div>
     <!--mobile menu-->
        <div class="mobile-menu hidden px-4 font-mulish">
            <a href="#" class=" block py-2 text-base">Home</a>
            <a href="#" class=" block py-2 text-base">Curriculum</a>
            <a href="#" class=" block py-2 text-base">Program</a>
            <a href="#" class=" block py-2 text-base text-brand-red-dark">Progress so far</a>
            <button class="bg-brand-red-dark hover:bg-white text-white hover:text-brand-red-dark font-normal py-4 text-base w-full">Join Zuri Training</button>
        
        </div>
    <div class="flex justify-center items-center lg:mt-10 md:mt-10 mt-10">
        <div class="border-0">
            <div class="font-normal font-mulish">
                <p class="text-brand-red-dark lg:text-2xl text-center md:text-2xl text-base text-center py-2">INTERNS PROGRESS TRACKER</p>
                <h2 class="text-brand-gray-dark-1 lg:text-md text-center md:text-md text-base lg:leading-10 md:leading-10 leading-2">GET TO KNOW HOW WELL OUR INTERNS ARE DOING<br>
                    AND WHERE THEY CURRENTLY ARE</h2>
            </div>
            <div class="font-normal text-center md:mt-7 lg:mt-7 font-mulish">
                <p class="text-brand-gray-dark-1 lg:text-2xl md:text-2xl text-base py-8">Subscribe to our newsletter today</p>
                <h2 class="text-brand-gray-light text-base mb-5">Get the latest information, news blog, conversations with our most talented
                <br>past interns and load of amazing information directly into your inbox</h2>
            </div>
            <div class="font-normal py-1 space-x-3 text-center justify-center lg:mb-10 md:mb-10 mb-5 font-mulish" > 
                <input type="email" placeholder="Enter your email address here" class="py-2 px-4 lg:w-4/6 md:w-4/6 w-5/6 bg-brand-red-light-1 border-solid border border-brand-gray-dark-1">
                <button class="bg-brand-gray-dark-1 hover:bg-white text-white hover:text-black font-normal lg:py-3 lg:px-6 md:py-3 md:px-6 mt-3 py-3 px-6 text-sm">Subscribe</button>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {
    data(){
        return{
       }
        },
        methods:{
            menu(){
                const menu = document.querySelector('.mobile-menu' )
                menu.classList.toggle("hidden");  

        }
   }
}
</script>

<style>

</style>