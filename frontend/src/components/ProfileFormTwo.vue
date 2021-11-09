<template>
    <div>
        <form action="">
            <div class="cursor-pointer flex justify-end pb-2" @click="toggleProfileEditModal">
            <img src="../assets/closeicon.svg" alt="" class="w-4 h-4 m-2"/>
        </div>
        <div class="block xs:flex justify-between items-center mb-4 xs:mb-10">
            <p style="color:red" v-if="this.$store.state.formTwoConfirmation" class="text-center">{{$store.state.statusMessage}}</p>
            <h1 class="text-2xl">EDIT PROFILE</h1>
                <p class="text-2xl text-brand-gray-light">2/2</p>
        </div>
        <div class="mb-3 sm:mb-5">
            <label>JOB TITLE</label><br>
            <input autocomplete type="text" v-model="position" placeholder="Enter your job title here" class="w-full text-brand-gray-light p-2 mt-1 sm:mt-3  border focus:outline-none border-black" >
        </div>
        <div class="block sm:flex justify-between gap-8">
            <div class="w-full mb-3 sm:mb-5">
                <label class="">COMPANY NAME</label><br>
                <input autocomplete type="text" v-model="company" placeholder="Enter organisation here" class="w-full text-brand-gray-light p-2 mt-1 sm:mt-3 border focus:outline-none border-black">
            </div>
            <div class="w-full mb-3">
                <label class="">DATE GOTTEN</label><br>
                <input autocomplete type="date" v-model="dateGotten" placeholder="Enter your current pay here" class="w-full text-brand-gray-light p-2 mt-1 sm:mt-3  border focus:outline-none border-black">
            </div>
        </div>
        <div class="w-full mb-3 sm:mb-5 sm:mr-12">
            <label class="">JOB DESCRIPTION</label><br>
            <textarea autocomplete v-model="jobDescription" placeholder="Tell us about your current job" class="w-full h-24 resize-none text-brand-gray-light p-2 mt-1 sm:mt-3 border border-black focus:outline-none"></textarea>
        </div>
        <div>
            <h1>COMPANY LOGO</h1>
            <img class="w-16 h-16 cursor-pointer" src="../assets/carbon_image.png" alt="">
            <input @change="upload" type="file" accept="image/*" id="image" />
        </div>
        </form>
    </div>
</template>

<script>
import {mapActions, mapMutations} from 'vuex'
import { mapFields } from 'vuex-map-fields';

export default {

    data(){
        return{
            item: {
                image: null,
                imagesArray: null
            },
            imageUrl: null,
    };
        
    },
    computed:{
        ...mapFields([
            'formTwo.position',
            'formTwo.company',
            'formTwo.dateGotten',
            'formTwo.jobDescription',
        ])
    },
    methods:{
        ...mapActions([
            'editJob'
        ]),
        ...mapMutations([
            'setImageTwo', "toggleProfileEditModal"
        ]),

        async uploadImage(e) {
        let image = e.target.files[0];
        const reader = new FileReader();
        reader.readAsDataURL(image);
        var myimage = await callBack(g)

        var g = "mockVariable"
        this.imageUrl = myimage
        this.setImageTwo(this.imageUrl)

        function callBack(g){
            console.log(g)
        return new Promise (function(resolve,reject){
            reader.onload = function(){
            resolve(reader.result);
            }
            reader.onerror = reject;
        })
        }

    },
    upload(e){
        let image = e.target.files[0];
        this.item.image = image;
        this.setImageTwo(this.item.image)
    }
    },

}
</script>