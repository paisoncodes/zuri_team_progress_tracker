<template>
    <div>
        <div class="">
                <div class="block xs:flex justify-between items-center mb-4 xs:mb-10">
                    <h1 class="text-2xl">SOJI AMINU'S PROFILE</h1>
                    <p class="text-2xl text-brand-gray-light">1/2</p>
                </div>
                
                 <div class="block sm:flex justify-between">
                        <div class="w-full mb-3 sm:mb-5 sm:mr-12">
                            <label class="">EDIT NAME</label><br>
                            <input type="text" v-model="Name" placeholder="Enter your name" class="w-full text-brand-gray-light p-2 mt-1 sm:mt-3 border focus:outline-none border-black">
                        </div>
                        <div class="w-full mb-3 sm:mb-5">
                            <label class="">CURRENT POSITION</label><br>
                            <input type="text" v-model="position" placeholder="Enter your current position here" class="w-full text-brand-gray-light p-2 mt-1 sm:mt-3 border focus:outline-none border-black">
                        </div>
                </div>
                <div class="w-full">
                    <div class="block sm:flex justify-between">
                        <div class="w-full mb-3 sm:mb-5 sm:mr-12">
                            <label class="">ORGANISATION NAME</label><br>
                            <input type="text" v-model="organisation1" placeholder="Enter organisation here" class="w-full text-brand-gray-light p-2 mt-1 sm:mt-3 border focus:outline-none border-black">
                        </div>
                        <div class="w-full mb-3 sm:mb-5">
                            <label class="">ORGANISATION NAME</label><br>
                            <input type="text" v-model="organisation2" placeholder="Enter organisation here" class="w-full text-brand-gray-light p-2 mt-1 sm:mt-3 border focus:outline-none border-black">
                        </div>
                    </div>
                    <div class="hidden sm:flex justify-between">
                        <div class="w-full mb-3 sm:mb-5 sm:mr-12">
                            <label class="">ORGANISATION NAME</label><br>
                            <input type="text" v-model="organisation3" placeholder="Enter organisation here" class="w-full text-brand-gray-light p-2 mt-1 sm:mt-3 border focus:outline-none border-black">
                        </div>
                        <div class="w-full mb-3 sm:mb-5">
                            <label class="">ORGANISATION NAME</label><br>
                            <input type="text" v-model="organisation4" placeholder="Enter organisation here" class="w-full text-brand-gray-light p-2 mt-1 sm:mt-3 border focus:outline-none border-black">
                        </div>  
                    </div>
                </div>
                <div class="text-blue-700 flex items-center cursor-pointer">
                    <p class="">Add more organisation</p>
                    <!-- Icon goes here -->
                </div>
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>