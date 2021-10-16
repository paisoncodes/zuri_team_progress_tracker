<template>
    <div>
        <div class="block xs:flex justify-between items-center mb-4 xs:mb-10">
            <h1 class="text-2xl">SOJI AMINU'S PROFILE</h1>
                <p class="text-2xl text-brand-gray-light">2/2</p>
        </div>
        <div class="mb-3 sm:mb-5">
            <label>JOB TITLE</label><br>
            <input type="text" v-model="position" placeholder="Enter your job title here" class="w-full text-brand-gray-light p-2 mt-1 sm:mt-3  border focus:outline-none border-black">
        </div>
        <div class="block sm:flex justify-between gap-8">
            <div class="w-full mb-3 sm:mb-5">
                <label class="">COMPANY NAME</label><br>
                <input type="text" v-model="company" placeholder="Enter organisation here" class="w-full text-brand-gray-light p-2 mt-1 sm:mt-3 border focus:outline-none border-black">
            </div>
            <div class="w-full mb-3">
                <label class="">DATE GOTTEN</label><br>
                <input type="text" v-model="position" placeholder="Enter your current pay here" class="w-full text-brand-gray-light p-2 mt-1 sm:mt-3  border focus:outline-none border-black">
            </div>
        </div>
        <div class="w-full mb-3 sm:mb-5 sm:mr-12">
            <label class="">JOB DESCRIPTION</label><br>
            <textarea v-model="about" placeholder="Tell us about your current job" class="w-full h-24 resize-none text-brand-gray-light p-2 mt-1 sm:mt-3 border border-black focus:outline-none"></textarea>
        </div>
        <div>
            <h1>COMPANY LOGO</h1>
            <img class="w-16 h-16 cursor-pointer" src="../assets/carbon_image.png" alt="">
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>