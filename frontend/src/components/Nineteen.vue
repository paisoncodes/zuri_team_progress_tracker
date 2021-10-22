<template>
  <div class="flex flex-col w-full text-center bg-white">
    <div class="pt-0">
      <div class="px-6 py-10 mx-auto max-w-7xl bg-brand-red-light-1">
        <MeetOurIntern :finalists="finalists" :totalCombinedSalary="totalCombinedSalary" :finalistDescription="finalistDescription"/>
        <InternProfile />
        <Interns />
        <FilterButton />
        <ExperienceTracker batch=2019 />
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
  name: "Nineteen",
  data() {
    return {
      finalists: 0,
      isFetchingFinalist: false,
      totalCombinedSalary: 0,
      isFetchingTotalCombinedSalary: false,
      finalistDescription: "Technology leads, society follows. The move towards increasing inclusivity and diversity in the industry through representation is of importance to me. I learned to observe and collaborate. I enjoy team work. I also know how to work remotely without difficulties. I give my best to any job i do. I am always interested in new and exciting projects. I am always ready to learn a new skill be it a new programming language or framework. I am determined to continue building beautiful user experiences and fighting for simplicity over complexity."
    }
  },
  methods: {
    getFinalists() {
      this.isFetchingFinalist = true;
      axios.get('https://zuri-progress-tracker.herokuapp.com/api/v1/statistics/batch/2019/').then(response => {
        this.finalists = response.data.finalists
        this.isFetchingFinalist = false;
      }).catch(() => {
        this.isFetchingFinalist = false;
      })
    },
    getTotalCombinedSalary() {
      this.isFetchingTotalCombinedSalary = true;
      axios.get('https://zuri-progress-tracker.herokuapp.com/api/v1/interns/batch/2019/total_salary/').then(response => {
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
