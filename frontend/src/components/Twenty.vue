<template>
  <div class="flex flex-col w-full text-center bg-white">
    <div class="pt-0">
      <div class="px-6 py-10 mx-auto max-w-7xl bg-brand-red-light-1">
        <MeetOurIntern :finalists="finalists" :totalCombinedSalary="totalCombinedSalary" :finalistDescription="finalistDescription" />
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
  name: "Twenty",
  data() {
    return {
      finalists: 0,
      isFetchingFinalist: false,
      totalCombinedSalary: 0,
      isFetchingTotalCombinedSalary: false,
      finalistDescription: "I'm obsessed with making things, even more obsessed with making things better. I am a web developer with the objective to ensure that your project goals are not only met but exceeded. I am very passionate about tech. Any idea big or small can be brought to life. I pride myself on the ability to take projects right from the concept,development stage through to the final production. I am excited to make the leap and continue refining my programming skills."
    }
  },
  methods: {
    getFinalists() {
      this.isFetchingFinalist = true;
      axios.get('https://zuri-progress-tracker.herokuapp.com/api/v1/statistics/batch/2020/').then(response => {
        this.finalists = response.data.finalists
        this.isFetchingFinalist = false;
      }).catch(() => {
        this.isFetchingFinalist = false;
      })
    },
    getTotalCombinedSalary() {
      this.isFetchingTotalCombinedSalary = true;
      axios.get('https://zuri-progress-tracker.herokuapp.com/api/v1/interns/batch/2020/total_salary/').then(response => {
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
