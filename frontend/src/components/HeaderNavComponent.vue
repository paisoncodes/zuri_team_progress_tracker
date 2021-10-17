<template>
<div class="w-full min-h-pth bg-brand-red-light-1 py-2">
    <div class="flex items-center justify-between py-6 px-6 mx-auto max-w-7xl ">

        <div class="text-base font-normal text-brand-gray-dark-1 font-mulish">ZURI.TEAM</div>

        <div class="hidden md:flex text-base space-x-5 items-center font-mulish">
            <a href="#">Home</a>
            <a href="#">Curriculum</a>
            <a href="#">Program</a>
            <a href="#" class="text-brand-red-dark">Progress so far</a>
            <button class="bg-brand-red-dark hover:bg-opacity-75 text-white font-normal px-6 py-2 text-sm">Join Zuri Training</button>
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
            <button class="bg-brand-red-dark hover:bg-opacity-75 text-white font-normal py-4 text-base w-full">Join Zuri Training</button>
        
        </div>
    <div class="flex justify-center items-center lg:mt-10 md:mt-10 mt-10">
        <div class="border-0">
            <div class="font-normal font-mulish">
                <p class="text-brand-red-dark lg:text-3xl text-center md:text-3xl text-base text-center py-2 font-medium">INTERNS PROGRESS TRACKER</p>
                <h2 class="text-brand-gray-dark-1 lg:text-md text-center md:text-md text-base lg:leading-10 md:leading-10 leading-2 font-medium">GET TO KNOW HOW WELL OUR INTERNS ARE DOING<br>
                    AND WHERE THEY CURRENTLY ARE</h2>
            </div>
            <div class="font-normal text-center md:mt-7 lg:mt-7 font-mulish">
                <p class="text-brand-gray-dark-1 lg:text-3xl md:text-3xl text-base py-8 font-medium">Subscribe to our newsletter today</p>
                <h2 class="text-brand-gray-light text-base mb-5">Get the latest information, news blog, conversations with our most talented
                <br>past interns and load of amazing information directly into your inbox</h2>
            </div>
            <div class="font-normal space-x-3 text-center justify-center lg:mb-10 md:mb-10 mb-5 font-mulish" v-on:submit.prevent="onSubscribe" > 
                <input type="email" placeholder="Enter your email address here" class="py-2 px-4 lg:w-4/6 md:w-4/6 w-5/6 bg-brand-red-light-1 border-solid border border-brand-gray-dark-1" name="subscriber_email"  v-model="subscriber_email">
                <button class="bg-brand-gray-dark-1 hover:bg-opacity-75 text-white font-normal lg:py-3 lg:px-6 md:py-3 md:px-6 mt-3 py-3 px-6 text-sm" v-on:click="onSubscribe()">Subscribe</button>
                <div class="flex justify-center">
                    <button id="hideMe" class="lg:w-3/6 md:w-3/6 w-11/12 rounded-md bg-brand-gray-dark-1 text-white font-semibold lg:py-3 lg:px-6 md:py-3 md:px-6 mt-3 py-3 px-3 text-center" v-if="isSubscribed"> Subscribed to ZURI.TEAM newsletter</button>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from "axios";

export default {
    data(){
        return{
            subscriber_email: '',
            isSubscribed: false,

         }
        },
        methods:{
            menu(){
                const menu = document.querySelector('.mobile-menu' )
                menu.classList.toggle("hidden");  
            },
            onSubscribe(){
                axios
                .post(
                    `https://zuri-progress-tracker.herokuapp.com/api/v1/subscribers/subscribe/`,
                    {subscriber_email: this.subscriber_email},
                    )
                    .then((response) => {
                        this.isSubscribed = true; 
                        console.log(response)
                        this.subscriber_email = ''
                        
                    });
            },
   }
}
</script>

<style>
   #hideMe{
   animation: hideAnimation 0s ease-in 4s;
   animation-fill-mode: forwards;
 }

@keyframes hideAnimation {
  to {
    visibility: hidden;
    width: 0;
    height: 0;
  }
}
</style>