<template>
  <div class="flex flex-col w-full text-center bg-white">
    <NavbarComponent />
    <Subscribe />

    <div class="pt-0">
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
import MeetOurIntern from "./MeetOurIntern.vue";
import InternProfile from "./InternProfile.vue";
import Interns from "./Interns.vue";
import FilterButton from "./FilterButton.vue";
import experinceTracker from "./experinceTracker.vue";

export default {
  components: {
    MeetOurIntern,
    InternProfile,
    Interns,
    FilterButton,
    experinceTracker,
  },
  name: "TwentyOne",
};
</script>

<style>

.pad-cont{
  margin-top: 4rem;
}
</style>
