<template>
    <div class="flex items-center justify-around max-w-6xl py-6 mx-auto bg-brand-red-light-1">
        <button class="py-2 text-sm font-normal text-white rounded-full bg-brand-red-dark hover:bg-white hover:text-brand-red-dark">
            All Stack (27,095)
        </button>
        <button class="px-6 py-2 text-sm font-normal border border-solid rounded-full bg-brand-red-light-1">
            HTML (3,853)
        </button>
        <button class="px-6 py-2 text-sm font-normal border border-2 border-solid rounded-full bg-brand-red-light-1">
            CSS (3,853)
        </button>
        <button class="px-6 py-2 text-sm font-normal border border-2 border-solid rounded-full bg-brand-red-light-1">
            Javascript (6,437)
        </button>
        <button class="px-6 py-2 text-sm font-normal border border-2 border-solid rounded-full bg-brand-red-light-1">
            UI/UX Design (7,787)
        </button>
        <button class="px-6 py-2 text-sm font-normal border border-2 border-solid rounded-full bg-brand-red-light-1">
            Java (924)
        </button>
    </div>
</template>

<script>
export default {
    name: 'FilterButton',
    data(){

    }
}
</script>

<style>
    .border {
        border: 1px solid #514949;
    }
</style>