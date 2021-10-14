<template>
<div class="w-4/5 mx-auto">
    <div class="flex bg-red-200 h-56">
        <div>This is the sidebar</div>
        <div class="flex-grow-1 bg-green-200">This is the main div</div>
    </div>
        <JobPlacement/>

</div>
</template>

<script>
import JobPlacement from '../components/jobPlacement.vue'

export default {
  components: { JobPlacement},

}
</script>

<style>

</style>