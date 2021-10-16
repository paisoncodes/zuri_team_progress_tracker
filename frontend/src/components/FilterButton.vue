<template>
    <div class="bg-brand-red-light-1" v-if="stacks">
      <div class="pt-2 pb-12 mb-8">
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-5">
          <button class="bg-brand-red-dark text-white hover:text-brand-red-light-3 font-normal sm:px-6 lg:px-2  py-2 rounded-full text-sm" @Click="AllStack">
            All Stack {{(stacks.length + 1)}}
          </button>
          <button class="bg-brand-red-light-1 border-solid border-2 hover:bg-brand-red-dark hover:text-white hover:border-white border-brand-gray-dark-1 font-normal sm:px-6 lg:px-2  py-2 rounded-full text-sm" @Click="HTML(stack)"
            v-for="(stack, index) in stacks"
            :key="index"
            :value="stack"
          > {{stack}}
          </button>
        </div>
      </div>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
    name: 'FilterButton',
    data(){
        return {
            data: {
              stack: ''
            }
          }
    },
    methods: {
        ...mapActions([
            'getAllStack',
            'getStack',
            'getTotalSalary'
        ]),
        AllStack() {
           this.getAllStack()
        },  
        HTML(stack) {
            this.getStack(stack)
        },
    }, 
    computed:{
          ...mapGetters({
            stacks: 'stacks',
          })
        },
    async created () {
        this.getTotalSalary()
        this.getAllStack()
    }
}
</script>

<style>

</style>