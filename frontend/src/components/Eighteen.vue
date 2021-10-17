<template>
  <div class="flex flex-col w-full text-center bg-white">
    <div class="pt-0">
      <div class="px-6 pt-10 mx-auto max-w-7xl bg-brand-red-light-1">
        <MeetOurIntern :finalists="finalists" :totalCombinedSalary="totalCombinedSalary"/>
        <InternProfile />
        <Interns />
        <FilterButton />
        <ExperienceTracker />
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
  name: "Eighteen",
    data() {
    return {
      finalists: 0,
      isFetchingFinalist: false,
      totalCombinedSalary: 0,
      isFetchingTotalCombinedSalary: false
    }
  },
  methods: {
    getFinalists() {
      this.isFetchingFinalist = true;
      axios.get('https://zuri-progress-tracker.herokuapp.com/api/v1/statistics/batch/2018/').then(response => {
        this.finalists = response.data.finalists
        this.isFetchingFinalist = false;
      }).catch(() => {
        this.isFetchingFinalist = false;
      })
    },
    getTotalCombinedSalary() {
      this.isFetchingTotalCombinedSalary = true;
      axios.get('https://zuri-progress-tracker.herokuapp.com/api/v1/interns/batch/2018/total_salary/').then(response => {
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
