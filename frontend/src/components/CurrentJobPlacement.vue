<template>
    <div class="bg-brand-red-light-2 p-6 m-0">
        <h2 class="cjb-heading text-left text-xs">CURRENT JOB PLACEMENTS</h2>
        
        <div class="relative pt-5">
            <div class="overflow-hidden h-5 text-lg flex rounded-xl bg-gray-200">
                <div :style="'width:' + progress_percent +'%'"
                    class="test-try shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-brand-gray-dark-1">
                </div>
            </div>
        </div>
        <p class="emp-status mt-5 text-left text-xs">{{total_employed}} / {{total_finalist}} Employed</p>
        
        <div class="flex flex-row justify-end align-middle">
            

            <div class="">
                <img class="inline-block align-middle px-0 my-5" v-for="intern in internPictures" v-bind:key="intern.id" v-bind:src="intern.picture" v-bind:alt="intern.alt">
            </div>
        </div>
    </div>
</template>

<script>

import {mapGetters, mapActions } from 'vuex'

    export default {
        name: 'CurrentJobPlacement',
        props:['total_finalist', 'total_employed'],
        data(){
            return {
                progress_percent: this.get_progress_percent(),
                new_total_employed: 0,
                new_total_finalist: 0
            }
        },
        methods:{
            get_progress_percent(){
                this.new_total_employed = this.total_employed
                this.new_total_finalist = this.total_finalist
                //console.log(this.new_total_employed, this.new_total_finalist)
                return (this.new_total_employed/this.new_total_finalist)*100
            },
            ...mapActions(['fetchInterns'])
        },
            computed: {
        ...mapGetters(["internPictures"])
        },
        mounted() {
        this.fetchInterns()
            },
        watch: {
            total_finalist (val, oldVal) {
              if (val !== oldVal){
                this.new_total_finalist = val;
              }
            },
            total_employed (val, oldVal) {
              if (val !== oldVal){
                this.new_total_employed = val;
                this.progress_percent = this.get_progress_percent()
              }
            }
        }
    }
</script>

<style scoped>

    .cjb-container {
        background: #F7F3F2;
        font-style: normal;
        font-weight: normal;
        font-size: 14px;
        line-height: 17px;
    }
    .cjb-heading {
        color: #A08F8F;
    }
    .cjb-month {
        color: #786B6B;
    }
    .emp-status {
        color: #786B6B;
    }

    span{
        width: 50%;
        margin: 5px;
    }

    img {
  border-radius: 50%;
  width: 42px;
  height: 42px;
}
</style>