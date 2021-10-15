<template>
<div class="max-w-6xl py-4 mx-auto">
    <div class="mb-2 text-left">
        <h2 class="text-2xl font-normal font-bold leading-loose text-gray-600 text-brand-gray-dark-1">Meet Our Interns</h2>
    </div>
    <div class="border"></div>
    <div class="mx-auto mt-2 sm:max-w-xl md:max-w-full lg:max-w-screen-xl">
      <div class="grid gap-6 lg:grid-cols-3">
        <div class="col-span-2">
            <div class="flex-col text-left">
              <h3 class="py-4 mb-2 text-base leading-tight text-brand-gray-light">HIGHLIGHTS</h3>
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
          <div class="flex-col mt-4 text-left">
            <h3 class="mb-2 text-base leading-tight text-brand-gray-light">KEY STATS</h3>
            <div class="flex flex-col lg:flex-row lg:items-center">
              <h1 class="px-0 text-2xl font-normal font-bold leading-loose text-gray-300 text-brand-gray-dark-1 tracker-wide lg:px-2">2,056,789</h1>
              <span class="text-base leading-tight uppercase text-brand-gray-light">Trained</span>
            </div>
            <div class="flex flex-col lg:flex-row lg:items-center">
              <h1 class="px-0 text-2xl font-normal font-bold leading-loose text-gray-300 text-brand-gray-dark-1 tracker-wide lg:px-2">$13,056,789</h1>
              <span class="text-base leading-tight uppercase text-brand-gray-light">In Montly Income</span>
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