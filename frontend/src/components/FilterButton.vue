<template>
    <div class="bg-brand-red-light-1" v-if="stacks">
      <div class="pt-2 pb-12 mb-8">
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-5">
          <button :class="{'bg-brand-red-dark text-white': stackContain.toString() == allStack.stack}" class="bg-brand-red-light-1 border-solid text-black border-2 border-brand-gray-dark-1 font-normal sm:px-6 lg:px-1 py-1 rounded-full text-sm" @Click="AllStack">
            All Stack {{(stacks.length)}}
          </button>
          <button :class="{'bg-brand-red-dark text-white': stackContain.toString() == stack}" class="bg-brand-red-light-1 border-solid border-2 border-brand-gray-dark-1 font-normal sm:px-6 lg:px-1 py-1 rounded-full text-sm" @Click="HTML(stack)"
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
            allStack: {
              stack: "allStack"
            },
            stackContain: []
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
            if(this.stackContain.length > 0) {
              this.stackContain.splice(0, 1, this.allStack.stack)
            }
        },  
        HTML(stack) {
            this.getStack(stack)

            if(this.stackContain.indexOf(stack) == -1) {
              this.stackContain.splice(0, 1, stack)
            } 
        },
        contains(arr, item) {
          return arr.indexOf(item) !== -1
        }
    }, 
    computed:{
          ...mapGetters({
            stacks: 'stacks',
          })
        },
    async created () {
        this.getAllStack()
        this.stackContain.splice(0, 1, this.allStack.stack)
    }
}
</script>

<style>
.clicked {
  background-color: bg-brand-red-dark;
}
</style>