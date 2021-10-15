<template>
    <div class="">
        <div class="absolute inset-y-0 inset-x-4  flex justify-center items-center">
            <form class="w-full max-w-2xl p-4 sm:p-7  text-brand-gray-dark-1">
                <keep-alive>
                    <component :is="component"></component>
                </keep-alive>
                <div :class="`mt-6 justify-end ${ component === 'FormTwo' ? 'hidden' : 'flex'}`">
                    <button @click.prevent="" type="submit" class="py-3 px-12 text-brand-gray-dark-1 border border-black mr-3">Cancel</button>
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
import FormOne from './ProfileFormOne.vue';
import FormTwo from './ProfileFormTwo.vue';
export default {
    components: {
        FormOne,
        FormTwo
    },
    data() {
        return {
            component: 'FormOne'
        }
    }
}
</script>