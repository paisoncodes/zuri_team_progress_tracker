<template>
  <div class="flex flex-col w-full text-center bg-white">
    <NavbarComponent />
    <Subscribe />

    <div class="pt-0">
      <div class="px-6 py-10 mx-auto max-w-7xl bg-brand-red-light-1">
        <MeetOurIntern />
        <InternProfile />
        <Interns />
        <FilterButton />
        <ExperienceTracker batch='2021' />
        <Footer />
      </div>
    </div>
  </div>
</template>

<script>
import MeetOurIntern from "@/components/MeetOurIntern.vue";
import InternProfile from "@/components/InternProfile.vue";
import Interns from "@/components/Interns.vue";
import FilterButton from "@/components/FilterButton.vue";
import ExperienceTracker from "@/components/ExperienceTracker.vue";

export default {
  components: {
    MeetOurIntern,
    InternProfile,
    Interns,
    FilterButton,
    ExperienceTracker,
  },
  name: "TwentyOne",
};
</script>

<style>
.pad-cont {
  margin-top: 4rem;
}
</style>
