<template>
<div>
  <div class="grid  md:grid-cols-4 sm:grid-cols-1   bg-brand-red-light-3 mb-5" v-for="(intern, index) in internTraker" :key="index" >
     <div class="icon w-full h-full ">
         <img class="object-cover object-center  h-full w-full" :src="intern.picture"/>
     </div>
     <div class="md:col-span-3 " >
      <div class="m-5" >
          <div class="grid md:grid-cols-2 sm:grid-cols-1  gap-4" >
          <div class="w-full text-brand-gray-dark-1 font-normal">
            <p class="text-xl">{{intern.name}}</p>
            <p class="text-base">{{intern.role}}</p>
          </div>
          <div class="w-full">
            <p class="leading-tight text-brand-gray-dark-2">{{intern.about}}</p>
          </div> 
        </div>
      <div>
        <h3  class="lg:my-4 text-brand-gray-dark-2">EXPERIENCE TRACKER</h3>
        
        <div class="overflow-x-scroll   overflow-hidden" > 
        <div class="tracker    ml-5 my-10 h-3 flex justify-between items-center text-brand-gray-dark-2 bg-brand-gray-dark-3">
          <div class="h-10 w-10 grid justify-items-center tracker-jobless">
            <div class="h-10 w-10  rounded-full bg-brand-gray-dark-3"> </div>
              <div >JOBLESS</div>
           
            </div>
              <div  class="relative bottom-4">2016</div>
            

            <div class="h-12 w-12 grid justify-items-center  relative">
              <img src="@/assets/paypal.png" class="border-solid border-2 border-brand-gray-dark-3 h-12 w-12 relative rounded-full" alt="">
                <div>PAYPAL</div>
            </div>
            <div  class="relative bottom-4" >2017</div>


            <div class="h-12 w-12 grid justify-items-center  relative">
              <img src="@/assets/flutterwave.png" class="h-12 w-12 relative border-solid border-2 border-brand-gray-dark-3 rounded-full" alt="">
                <div>FLUTTERWAVE</div>
            </div>
             <div  class="relative bottom-4" >2018</div>


            <div class="h-12 w-12 grid justify-items-center relative">
              <img src="@/assets/paystack.png" class="h-12 w-12 border-solid border-2 border-brand-gray-dark-3  relative rounded-full" alt="">
                <div class="relative">PAYSTACK</div>
            </div>
            <div  class="relative bottom-4 " >2019</div>

              <div class="h-20 w-20 grid justify-items-center relative rounded-full">
              <img src="@/assets/hotels.png" class="h-20 w-20 border-solid border-2 border-brand-gray-dark-1  relative rounded-full" alt="">
            </div>

        </div>
        </div>
        <p class="float-right text-blue-500 cursor-pointer mb-3">Edit</p>
      </div>
      </div>
      </div>
  </div>
  </div>
</template>

<script>
export default {
  data(){
    return {
      internTraker:[
        {
          name:"Soji Aminu",
          role: 'Senior Digital Product Designer @andela',
           picture: require('../assets/soji.png'),
           about: 'An exceptional product designer with years of experience understanding the users thinking pattern and this helps in creating user centered product.'
        }, 
        {
          name:"Soji Aminu",
          role: 'Senior Digital Product Designer @andela',
           picture: require('../assets/soji.png'),
           about: 'An exceptional product designer with years of experience understanding the users thinking pattern and this helps in creating user centered product.'
        },
        {
          name:"Soji Aminu",
          role: 'Senior Digital Product Designer @andela',
           picture: require('../assets/soji.png'),
           about: 'An exceptional product designer with years of experience understanding the users thinking pattern and this helps in creating user centered product.'
        },
        {
          name:"Soji Aminu",
          role: 'Senior Digital Product Designer @andela',
           picture: require('../assets/soji.png'),
           about: 'An exceptional product designer with years of experience understanding the users thinking pattern and this helps in creating user centered product.'
        },
      ]
    }
  }
}
</script>

<style  scoped>
  .tracker{
    width:600px;
  }
  .tracker-jobless{
    margin-left:-2%
  }

  
/* custom scrollbar */
/* width */
::-webkit-scrollbar {
  width: 2px;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #514949; 
  border-radius: 10px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #898989; 
}


</style>