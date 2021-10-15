<template>

  <div class="flex flex-col w-full text-center bg-white">
  
    <NavbarComponent/>
    <Subscribe/>
    <TwentyOneContainer/>
      <div class="px-6 py-10 mx-auto max-w-7xl bg-brand-red-light-1">
   
    <MeetOurIntern />
    <InternProfile />
    <Interns />
    <FilterButton />
    <ExperinceTracker />
    <Footer />
    </div>
  </div>

</template>

<script>
import NavbarComponent from '../components/NavbarComponent.vue'
import Subscribe from '../components/Subscribe.vue'
import TwentyOneContainer from '../components/TwentyOneContainer.vue'
import MeetOurIntern from '../components/MeetOurIntern.vue'
import InternProfile from '../components/InternProfile.vue'
import Interns from '../components/Interns.vue'
import FilterButton from '../components/FilterButton.vue'
import ExperinceTracker from '../components/ExperinceTracker.vue'
import Footer from '../components/Footer.vue'

export default {
  components: { NavbarComponent, Subscribe, TwentyOneContainer, MeetOurIntern, InternProfile, Interns, FilterButton, ExperinceTracker, Footer},
  name: 'TwentyOne',
}
</script>

