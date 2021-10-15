<template>
    <div class="bg-brand-red-light-2 p-6 m-0">
        <h2 class="cjb-heading text-left text-xs">CURRENT JOB PLACEMENTS</h2>
        <div class="flex justify-between">
            <div class="cjb-month mt-5 text-sm">January</div>
            <div class="cjb-month mt-5 text-sm">December</div>
        </div>
        <div class="relative pt-5">
            <div class="overflow-hidden h-5 text-lg flex rounded-xl bg-gray-200">
                <div style="width:60%"
                    class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-brand-gray-dark-1">
                </div>
            </div>
        </div>
        <p class="emp-status mt-5 text-left text-xs">1,54500,000 / 2,056,789 Employed</p>
        <div class="mt-10 mb-8 text-brand-gray-blue text-left">
            <h2 class="text-xs"><a href="#">VIEW COMPLETE PROGRESS ></a></h2>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'CurrentJobPlacement'
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
</style>