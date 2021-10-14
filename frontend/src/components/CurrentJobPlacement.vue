<template>
    <div class="cjb-container p-6">
        <h2 class="cjb-heading text-left">CURRENT JOB PLACEMENTS</h2>
        <div class="flex justify-between">
            <div class="cjb-month mt-5">January</div>
            <div class="cjb-month mt-5">December</div>
        </div>
        <div class="relative pt-5">
            <div class="overflow-hidden h-5 text-lg flex rounded-xl bg-gray-200">
                <div style="width:60%"
                    class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-brand-gray-dark-1">
                </div>
            </div>
        </div>
        <p class="emp-status mt-5 text-left">1,54500,000 / 2,056,789 Employed</p>
        <h2 class="cjb-heading mt-10 text-left">WHERE SOME OF OUR</h2>
        <h2 class="cjb-heading mt-2 text-left">INTERNS NOW WORK</h2>

        <div class="flex mt-5">
            <span>
                <img src="@/assets/CurrentJobPlacement/company_1.png">
            </span>
            <span>
                <img src="@/assets/CurrentJobPlacement/company_2.png">
            </span>
            <span>
                <img src="@/assets/CurrentJobPlacement/company_3.png">
            </span>
            <span>
                <img src="@/assets/CurrentJobPlacement/company_4.png">
            </span>
            <span>
                <img src="@/assets/CurrentJobPlacement/company_5.png">
            </span>
            <span>
                <img src="@/assets/CurrentJobPlacement/company_6.png">
            </span>
            <span>
                <img src="@/assets/CurrentJobPlacement/company_7.png">
            </span>
            <span>
                <img src="@/assets/CurrentJobPlacement/company_8.png">
            </span>
        </div>

        <div class="mt-10 mb-8 text-brand-gray-blue text-left">
            <h2><a href="#">VIEW COMPLETE PROGRESS ></a></h2>
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