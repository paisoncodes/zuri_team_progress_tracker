<template>
<div class="mx-auto w-4/5 bg-brand-red-light-1 py-4 px-6">
    <div class="text-left mb-2">
        <h2 class="text-2xl font-normal leading-loose text-gray-600 font-bold text-brand-gray-dark-1">Meet Our Interns</h2>
    </div>
    <div class="border"></div>
    <div class="mt-2 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl">
      <div class="grid gap-6 lg:grid-cols-3">
        <div class="col-span-2">
            <div class="flex-col text-left">
              <h3 class="mb-2 text-brand-gray-light leading-tight text-base py-4">HIGHLIGHTS</h3>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                 Integer elit dictumst mauris aenean id vitae ut augue 
                 aliquam. Aliquam diam, id diam egestas. A est fringilla 
                 amet malesuada gravida id. Sed fringilla morbi vitae 
                 nunc ultrices diam bibendum quisque. Elit aliquet 
                 tristique neque, amet urna, ultrices at. Ullamcorper 
                 ultricies ante at lorem tincidunt. Turpis arcu, iaculis 
                 at nisi sit. Fermentum feugiat ut euismod imperdiet sed 
                 porta netus nulla. Lectus amet mollis dui eget pretium 
                 semper dictumst netus. 
              </p>
            </div>
        </div>
        <div>
          <div class="flex-col text-left mt-4">
            <h3 class="mb-2 text-brand-gray-light leading-tight text-base">KEY STATS</h3>
            <div class="flex flex-col lg:flex-row lg:items-center">
              <h1 class="text-2xl font-normal leading-loose text-gray-300 font-bold text-brand-gray-dark-1 tracker-wide px-0 lg:px-2">2,056,789</h1>
              <span class="uppercase text-brand-gray-light leading-tight text-base">Trained</span>
            </div>
            <div class="flex flex-col lg:flex-row lg:items-center">
              <h1 class="text-2xl font-normal leading-loose text-gray-300 font-bold text-brand-gray-dark-1 tracker-wide px-0 lg:px-2">$13,056,789</h1>
              <span class="uppercase text-brand-gray-light leading-tight text-base">In Montly Income</span>
            </div>
          </div>
        </div>
      </div>
    </div>
</div>
</template>

<script>
export default {
  name: 'MeetOurIntern',
  data(){
    return {
    }
  },
  
}
</script>

<style>
    .border {
        border-bottom: 1px thin #898989;
    }
</style>