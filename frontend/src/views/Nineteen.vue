<template>
  <div class="flex flex-col w-full text-center bg-white">
    <NavbarComponent />
    <Subscribe />

    <div class="py-8">

      <nav class="flex flex-col text-sm sm:flex-row mx-auto max-w-7xl">
          <button class="block py-4 text-brand-gray-light mx-auto w-1/6 hover:text-brand-gray-dark-1 focus:outline-none">
              OVERVIEW 
          </button>
          
          <button class="block py-4 text-brand-gray-light mx-auto w-1/6 hover:text-brand-gray-dark-1 focus:outline-none">
              2021 <br> (10,000 interns)
          </button>
          
          <button class="block py-4 text-brand-gray-light mx-auto w-1/6 hover:text-brand-gray-dark-1 focus:outline-none">
              2020 <br> (10,000 interns)
          </button>
          
          <button class="block py-4 font-medium bg-brand-red-light mx-auto hover:text-blue-500 focus:outline-none text-brand-gray-dark-1 border-brand-gray-light bg-brand-red-light-1 w-1/6">
              2019 <br> (10,000 interns)
          </button>
          <button class="block py-4 text-brand-gray-light w-1/6 mx-auto hover:text-brand-gray-dark-1 focus:outline-none">
              2018 <br> (10,000 interns)
          </button>
      </nav>
    
      <div class="px-6 py-10 mx-auto max-w-7xl bg-brand-red-light-1 ">
        <MeetOurIntern />
        <InternProfile />
        <Interns />
        <FilterButton />
        <experinceTracker />
        <Footer />
      </div> 
    </div>
  </div>
</template>

<script>
import NavbarComponent from "../components/NavbarComponent.vue";
import Subscribe from "../components/Subscribe.vue";
import MeetOurIntern from "../components/MeetOurIntern.vue";
import InternProfile from "../components/InternProfile.vue";
import Interns from "../components/Interns.vue";
import FilterButton from "../components/FilterButton.vue";
import experinceTracker from "../components/experinceTracker.vue";
import Footer from "../components/Footer.vue";

export default {
  components: {
    NavbarComponent,
    Subscribe,
    MeetOurIntern,
    InternProfile,
    Interns,
    FilterButton,
    experinceTracker,
    Footer,
  },
  name: "Nineteen",
};
</script>

<style>

.pad-cont{
  margin-top: 4rem;
}
</style>
