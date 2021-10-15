<template>
    <div>
        <div class="block xs:flex justify-between items-center mb-4 xs:mb-10">
            <h1 class="text-2xl">SOJI AMINU'S PROFILE</h1>
                <p class="text-2xl text-brand-gray-light">2/2</p>
        </div>
        <div class="mb-3 sm:mb-5">
            <label>ENTER YOUR SALARY</label><br>
            <input type="text" v-model="salary" placeholder="Enter your current pay here" class="w-full text-brand-gray-light p-2 mt-1 sm:mt-3  border focus:outline-none border-black">
            <p class="text-brand-gray-light mt-1.5">Note: Salary details will be kept private</p>
        </div>

        <div class="mb-3">
            <label class="">ABOUT YOU</label><br>
            <textarea v-model="about" placeholder="Express things about you" class="w-full h-24 resize-none text-brand-gray-light p-2 mt-1 sm:mt-3 border border-black focus:outline-none"></textarea>
        </div>
        <div>
            <h1>UPLOAD IMAGE</h1>
            <img class="w-16 h-16 cursor-pointer" src="../assets/carbon_image.png" alt="">
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>