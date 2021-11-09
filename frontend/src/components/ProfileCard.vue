<template>
    <div class="mx-auto z-50 text-left">
        <div @click="toggleModal()" class="fixed inset-y-0 inset-x-0  flex justify-center items-center bg-black bg-opacity-50">
            <form @click.stop="" class="w-full max-w-2xl p-4 sm:p-7 z-10 text-brand-gray-dark-1 bg-white">
                <keep-alive>
                    <component :is="component"></component>
                </keep-alive>
                <div :class="`mt-6 justify-end ${ component === 'FormTwo' ? 'hidden' : 'flex'}`">
                    <button @click.prevent="editIntern" type="submit" class="py-3 px-12 text-brand-gray-dark-1 border border-black mr-3 hover:bg-brand-gray-light
                  hover:text-white">Save</button>
                    <button @click.prevent="component = 'FormTwo'" type="submit" class="py-3 px-12 bg-brand-gray-dark-1 text-white border border-brand-gray-dark-1 hover:bg-brand-gray-light
                  hover:text-white">Add job</button>
                </div>
                <div :class="`mt-6 justify-end ${ component === 'FormOne' ? 'hidden' : 'flex' }`">
                    <button  @click.prevent="toggleModal()" type="submit" class="py-3 px-12 text-brand-gray-dark-1 border border-black mr-3 hover:bg-brand-gray-light
                  hover:text-white">Cancel</button>
                    <button @click.prevent="postJob" type="submit" class="py-3 px-12 bg-brand-gray-dark-1 text-white border border-brand-gray-dark-1 hover:bg-brand-gray-light
                  hover:text-white">Save</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import FormOne from '@/components/ProfileFormOne.vue';
import FormTwo from '@/components/ProfileFormTwo.vue';
import {mapActions} from 'vuex';
export default {
    components: {
        FormOne,
        FormTwo
    },
    data() {
        return {
            component: 'FormOne',
        }
    },
    methods:{
        toggleModal() {
        this.$store.commit('toggleProfileEditModal');
        this.component = 'FormOne'
        },
        ...mapActions([
            'editIntern',
            'postJob'
        ]),

    }
}
</script>