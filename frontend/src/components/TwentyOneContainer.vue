<template>
  <div class="py-8">

    <div class="px-6 py-10 mx-auto max-w-7xl bg-brand-red-light-1">
      <MeetOurIntern />
      <InternProfile />
      <Interns />
      <FilterButton />
      <ExperienceTracker />
      <Footer />
    </div>
  </div>
</template>

<script>
import MeetOurIntern from "@/components/MeetOurIntern.vue";
import InternProfile from "@/components/InternProfile.vue";
import Interns from "@/components/Interns.vue";
import FilterButton from "@/components/FilterButton.vue";
import ExperienceTracker from "@/components/ExperienceTracker.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "TwentyOneContainer.vue",
  components: {
    MeetOurIntern,
    InternProfile,
    Interns,
    FilterButton,
    ExperienceTracker,
    Footer,
  },
};
</script>