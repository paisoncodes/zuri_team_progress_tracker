<template>
  <div class="flex flex-col w-full text-center bg-white">
    <div class="px-6 py-10 mx-auto max-w-7xl bg-brand-red-light-1">
      <MeetOurIntern :finalists="finalists" :totalCombinedSalary="totalCombinedSalary" :finalistDescription="finalistDescription"/>
      <InternProfile />
      <Interns />
      <FilterButton />
      <ExperienceTracker />
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
      finalistDescription: "After a professional internship program lasting several weeks, a selection of the very best interns was made from a pool of talented individuals ranging from designers to developers to digital marketers etc. These finalists have proven to be competent in their various fields of expertise and are ready to join the workforce to solve critical world problems."
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
        this.totalCombinedSalary = new Intl.NumberFormat("en-US").format(response.data.total_salary)
        this.isFetchingTotalCombinedSalary = false;
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