<template>
<div>
  <div class="flex bg-brand-red-light-3 text-justify my-5" v-for="(intern, index) in internTraker" :key="index">
     <div class="icon w-50 h-50">
         <img class="object-cover h-full w-full" :src="intern.picture"/>
     </div>
      <div class="p-5" >
          <div class="flex flex-row items-center w-1/3 w-full">
          <div class="w-full text-brand-gray-dark-1 font-medium">
            <h2>{{intern.name}}</h2>
            <p>{{intern.role}}</p>
          </div>
          <div class="w-full">
            <p class="text-brand-gray-dark-2">{{intern.about}}</p>
          </div> 
        </div>
      <div>
        <h3  class="text-brand-gray-dark-2">EXPERIENCE TRACKER</h3>
        <!-- tracker -->   
        <div class="tracker ml-5 my-10 h-3 flex justify-between items-center text-brand-gray-dark-2 bg-brand-gray-dark-3">
          <div class="h-10 w-10 grid justify-items-center tracker-jobless">
            <div class="h-10 w-10  rounded-full bg-brand-gray-dark-3"> </div>
              <div class="relative">JOBLESS</div>
           
            </div>
              <div  class="relative bottom-4">2016</div>
            

            <div class="h-12 w-12 grid justify-items-center  relative">
              <img src="@/assets/paypal.png" class="border-solid border-2 border-brand-gray-dark-3 h-12 w-12 relative rounded-full" alt="">
                <div class="relative">PAYPAL</div>
            </div>
            <div  class="relative bottom-4" >2017</div>


            <div class="h-12 w-12 grid justify-items-center  relative">
              <img src="@/assets/flutterwave.png" class="h-12 w-12 relative border-solid border-2 border-brand-gray-dark-3 rounded-full" alt="">
                <div class="relative">FLUTTERWAVE</div>
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
        <p class="float-right text-blue">Edit</p>
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

<style scoped>
  .tracker{
    width:70%;
  }
  .tracker-jobless{
    margin-left:-2%
  }
</style>