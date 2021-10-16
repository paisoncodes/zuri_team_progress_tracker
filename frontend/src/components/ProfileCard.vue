<template>
    <div class="mx-auto z-50">
        <div @click="toggleModal()" class="fixed inset-y-0 inset-x-0  flex justify-center items-center bg-black bg-opacity-50">
            <form @click.stop="" class="w-full max-w-2xl p-4 sm:p-7 z-10 text-brand-gray-dark-1 bg-white">
                <keep-alive>
                    <component :is="component"></component>
                </keep-alive>
                <div :class="`mt-6 justify-end ${ component === 'FormTwo' ? 'hidden' : 'flex'}`">
                    <button @click.prevent="" @click="toggleModal()" type="submit" class="py-3 px-12 text-brand-gray-dark-1 border border-black mr-3">Cancel</button>
                    <button @click.prevent="component = 'FormTwo'" type="submit" class="py-3 px-12 bg-brand-gray-dark-1 text-white border border-brand-gray-dark-1">Next</button>
                </div>
                <div :class="`mt-6 justify-end ${ component === 'FormOne' ? 'hidden' : 'flex' }`">
                    <button @click.prevent="component = 'FormOne'" type="submit" class="py-3 px-12 text-brand-gray-dark-1 border border-black mr-3">Back</button>
                    <button @click.prevent="" type="submit" class="py-3 px-12 bg-brand-gray-dark-1 text-white border border-brand-gray-dark-1">Save</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import FormOne from '@/components/ProfileFormOne.vue';
import FormTwo from '@/components/ProfileFormTwo.vue';
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
        },
    }
}
</script>