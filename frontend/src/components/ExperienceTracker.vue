<template>
<div class="text-left mx-auto md:w-full">
  <div class="grid  md:grid-cols-4 sm:grid-cols-1   bg-brand-red-light-3 mb-5" v-for="(intern, index) in getAllInterns" :key="index" >
     <!-- <div class="icon" style=" width:inherit; height:100%;">
         <img class="object-contain object-center  h-full w-full" style="width:inherit; height:100%;" :src="intern.picture"/>
     </div> -->
     
      <div class="icon h-72 rounded" :style="{ backgroundImage: `url('${intern.picture}')` }">
         <!-- <img class="object-contain object-center  h-full w-full"/> -->
     </div>

     <div class="md:col-span-3 ">
      <div class="mx-5 mt-5"  >
          <div class="grid md:grid-cols-2  gap-4" >
          <div class="w-full text-brand-gray-dark-1 font-normal">
            <p class="text-xl">{{intern.full_name}}</p>
            <p class="text-base">{{intern.stack.join(', ')}}</p>
          </div>
          <div class="w-full">
            <p class="leading-tight text-brand-gray-dark-2">{{intern.about}}</p>
          </div> 
        </div>
      <div >
        <h3  class="my-4 text-brand-gray-dark-2">EXPERIENCE TRACKER</h3>
        
        <div class="tracker_overflow py-3" > 
        <div  class="tracker    ml-10 my-10 h-3 flex justify-between items-center text-brand-gray-dark-2 bg-brand-gray-dark-3">
          <div class="h-10 w-10 relative grid justify-items-center tracker-jobless">
            <div class="h-10 w-10  rounded-full bg-brand-gray-dark-3"> </div>
              <div class="absolute top-11">JOBLESS</div>
           
            </div>
              <div  class="relative  bottom-4">2016</div>
            

            <div class="h-12 w-12 relative grid justify-items-center ">
              <img src="@/assets/paypal.png" class="border-solid border-2 border-brand-gray-dark-3 h-12 w-12  rounded-full" alt="">
                <div class="absolute top-12">PAYPAL</div>
            </div>
            <div  class="relative bottom-4" >2017</div>

            

            <div class="h-12 w-12 relative  grid justify-items-center ">
              <img src="@/assets/flutterwave.png" class="h-12 w-12 border-solid border-2 border-brand-gray-dark-3 rounded-full" alt="">
                <div class="absolute top-12">FLUTTERWAVE</div>
            </div>
             <div  class="relative bottom-4" >2018</div>


            <div class="h-12 w-12 relative grid justify-items-center">
              <img src="@/assets/paystack.png" class="h-12 w-12 border-solid border-2 border-brand-gray-dark-3  rounded-full" alt="">
                <div class="absolute top-12">PAYSTACK</div>
            </div>
            <div  class="relative bottom-4 " >2019</div>

              <div class="h-20 w-20 grid justify-items-center relative">
              <img src="@/assets/hotels.png" class="h-20 w-20 border-solid border-2 border-brand-gray-dark-1  rounded-full" alt="">
            </div>

        </div>
        </div>
        <p @click="showLogin(intern.id)" class="float-right text-blue-500 cursor-pointer w-100 flex mb-3"  >
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M14 1L19 6L6 19H1V14L14 1Z" stroke="#4774E8" stroke-width="1.22693" stroke-linecap="round" stroke-linejoin="round"/>
          </svg> <span class="ml-3">Edit</span>
          </p>
      </div>
      </div>
      </div>
  </div>

  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { mapActions } from 'vuex'
export default {
  
  data(){
    return {
      internTraker:[
        {
          name:"Soji Aminu",
          role: 'Senior Digital Product Designer @andela',
           picture: require('../assets/soji.png'),
           about: 'An exceptional product designer with years of experience understanding the users thinking pattern and this helps in creating user centered product.',
           experience:[
             {
               year:'2016',
               state:'0',
               companyName:'JOBLESS',
               companyIcon:'',
             },
             {
               year:'2017',
               state:'1',
               companyName:'PAYPAL',
               companyIcon:require('../assets/hotels.png'),
             },
             {
               year:'2018',
               state:'0',
               companyName:'FLUTTERWAVE',
               companyIcon:require('../assets/flutterwave.png'),
             },
              {
               year:'2019',
               state:'0',
               companyName:'FLUTTERWAVE',
               companyIcon:require('../assets/flutterwave.png'),
             },
             {
               year:'2020',
               state:'0',
               companyName:'HOTELS',
               companyIcon:require('../assets/flutterwave.png'),
             }
           ]
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
      ],
      internjobs:[]
    }
  },
 computed: {
        ...mapGetters({
             getAllInterns: 'allInterns',
             userJob:'allUserjobs',
        })
    },
methods:{
    ...mapActions({
      interns: 'getAllStack',
      internJob: 'getUserJob'
    }),
  showLogin(intern_id){
    this.$store.commit('currentUserId',intern_id);
    this.eventBus.emit('toggleLoginModal', true);

  },
internsJobs(){
  this.getAllInterns.forEach(element => {
   this.internJob(element.id)
  });
  // console.log(this.userJob)
},

},
async created() {
 await this.interns().then(()=>{
   this.internsJobs()
 })
}
}
</script>

<style  scoped>
.icon{
  background-repeat: no-repeat;  
  background-size:cover; 
  background-position: center;
  /* height:30; */
}
  .tracker{
    width:600px;
  }
  .tracker_overflow{

  min-width: 100%;
  width:1rem;
  overflow-x: scroll;
  overflow-y: hidden;
  }
  .tracker-jobless{
    margin-left:-3%
  }

  
/* custom scrollbar */
/* width */
::-webkit-scrollbar {
  width: 16px;
  height: 5px;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #898989; 
  border-radius: 10px;
  scrollbar-width: thin;
}

/* ::-webkit-scrollbar-track { */
    /* background-color: darkgrey; */

/* } */
/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #514949; 
transition:all 4s;

}


</style>