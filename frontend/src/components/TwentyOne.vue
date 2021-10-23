<template>
  <div class="flex flex-col w-full text-center bg-white">
    <NavbarComponent />
    <Subscribe />

    <div class="pt-0">
      <div class="px-6 py-10 mx-auto max-w-7xl bg-brand-red-light-1">
        <MeetOurIntern :finalists="finalists" :totalCombinedSalary="totalCombinedSalary" :finalistDescription="finalistDescription"/>
        <InternProfile />
        <Interns />
        <FilterButton />
        <ExperienceTracker />
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
import axios from "axios";

export default {
  components: {
    MeetOurIntern,
    InternProfile,
    Interns,
    FilterButton,
    ExperienceTracker,
  },
  name: "TwentyOne",
  data() {
    return {
      finalists: 0,
      isFetchingFinalist: false,
      totalCombinedSalary: 0,
      isFetchingTotalCombinedSalary: false,
      finalistDescription: "A key player in his field. He proved himself to be dedicated and focused in all his endeavours. Having mastered the art of programming, he came out in flying colors as one of our best performing interns. With daily activites such coding and test programming for software and mobile apps, he is defining his space in the tech industry. He is proficient in several languagues such as Javascript, Python and PHP. He also has great communication skills and he has proven himself to be a true leader amongst his peers."
    }
  },
  methods: {
    getFinalists() {
      this.isFetchingFinalist = true;
      axios.get('https://zuri-progress-tracker.herokuapp.com/api/v1/statistics/batch/2021/').then(response => {
        this.finalists = response.data.finalists
        this.isFetchingFinalist = false;
      }).catch(() => {
        this.isFetchingFinalist = false;
      })
    },
    getTotalCombinedSalary() {
      this.isFetchingTotalCombinedSalary = true;
      axios.get('https://zuri-progress-tracker.herokuapp.com/api/v1/interns/batch/2021/total_salary/').then(response => {
        this.totalCombinedSalary = response.data.total_salary
        this.isFetchingTotalCombinedSalary = false;
        console.log(this.totalCombinedSalary);
      }).catch(() => {
        this.isFetchingTotalCombinedSalary = false;
      })
    }
  },
  mounted() {
    this.getFinalists();
    this.getTotalCombinedSalary();
  },
};
</script>

<style>
.pad-cont {
  margin-top: 4rem;
}
</style>
