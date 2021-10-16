<template>
    <div class="bg-brand-red-light-1">
      <div class="py-6">
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-5">
          <button class="bg-brand-red-dark hover:bg-white text-white hover:text-brand-red-dark font-normal sm:px-6 lg:px-2  py-2 rounded-full text-sm" @Click="AllStack">
            All Stack (27,095)
          </button>
          <button class="bg-brand-red-light-1 border-solid border-2 border font-normal sm:px-6 lg:px-2  py-2 rounded-full text-sm" @Click="HTML">
            HTML (3,853)
          </button>
          <button class="bg-brand-red-light-1 border-solid border-2 border font-normal sm:px-6 lg:px-2  py-2 rounded-full text-sm" @Click="CSS">
            CSS (3,853)
          </button>
          <button class="bg-brand-red-light-1 border-solid border-2 border font-normal sm:px-6 lg:px-2  py-2 rounded-full text-sm" @Click="Javascript">
            Javascript (6,437)
          </button>
          <button class="bg-brand-red-light-1 border-solid border-2 border font-normal sm:px-6 lg:px-2 py-2 rounded-full text-sm" @Click="UiUx">
            UI/UX Design (7,787)
          </button>
          <button class="bg-brand-red-light-1 border-solid border-2 border font-normal sm:px-6 lg:px-2  py-2 rounded-full text-sm" @Click="Java">
            Java (924)
          </button>
        </div>
      </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
    name: 'FilterButton',
    data(){

    },
    methods: {
        ...mapActions([
            'getStack',
            
        ]),
        AllStack() {
           this.getStack('allStack');
        },  
        HTML() {
            this.getStack('html')
        },
        CSS() {
            this.getStack('css')
        },
        Javascript() {
            this.getStack('Javascript')
        },
        UiUx() {
            this.getStack('uiux')
        },
        Java() {
            this.getStack('java')
        }
    },
    async created () {

    }
}
</script>

<style>
    .border {
        border: 1px solid #514949;
    }
</style>