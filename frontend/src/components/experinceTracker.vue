<template>
  <div class="max-w-6xl mx-auto">
    <div
      class="flex my-5 text-justify bg-brand-red-light-3"
      v-for="(intern, index) in internTraker"
      :key="index"
    >
      <div class="icon w-50 h-50">
        <img class="object-cover w-full h-full" :src="intern.picture" />
      </div>
      <div class="p-5">
        <div class="flex flex-row items-center w-1/3 w-full">
          <div class="w-full font-medium text-brand-gray-dark-1">
            <h2>{{ intern.name }}</h2>
            <p>{{ intern.role }}</p>
          </div>
          <div class="w-full">
            <p class="text-brand-gray-dark-2">{{ intern.about }}</p>
          </div>
        </div>
        <div>
          <h3 class="text-brand-gray-dark-2">EXPERIENCE TRACKER</h3>
          <!-- tracker -->
          <div
            class="
              flex
              items-center
              justify-between
              h-3
              my-10
              ml-5
              tracker
              text-brand-gray-dark-2
              bg-brand-gray-dark-3
            "
          >
            <div class="grid w-10 h-10 justify-items-center tracker-jobless">
              <div class="w-10 h-10 rounded-full bg-brand-gray-dark-3"></div>
              <div class="relative">JOBLESS</div>
            </div>
            <div class="relative bottom-4">2016</div>

            <div class="relative grid w-12 h-12 justify-items-center">
              <img
                src="@/assets/paypal.png"
                class="
                  relative
                  w-12
                  h-12
                  border-2 border-solid
                  rounded-full
                  border-brand-gray-dark-3
                "
                alt=""
              />
              <div class="relative">PAYPAL</div>
            </div>
            <div class="relative bottom-4">2017</div>

            <div class="relative grid w-12 h-12 justify-items-center">
              <img
                src="@/assets/flutterwave.png"
                class="
                  relative
                  w-12
                  h-12
                  border-2 border-solid
                  rounded-full
                  border-brand-gray-dark-3
                "
                alt=""
              />
              <div class="relative">FLUTTERWAVE</div>
            </div>
            <div class="relative bottom-4">2018</div>

            <div class="relative grid w-12 h-12 justify-items-center">
              <img
                src="@/assets/paystack.png"
                class="
                  relative
                  w-12
                  h-12
                  border-2 border-solid
                  rounded-full
                  border-brand-gray-dark-3
                "
                alt=""
              />
              <div class="relative">PAYSTACK</div>
            </div>
            <div class="relative bottom-4">2019</div>

            <div
              class="relative grid w-20 h-20 rounded-full justify-items-center"
            >
              <img
                src="@/assets/hotels.png"
                class="
                  relative
                  w-20
                  h-20
                  border-2 border-solid
                  rounded-full
                  border-brand-gray-dark-1
                "
                alt=""
              />
            </div>
          </div>
          <p class="float-right text-blue">Edit</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "experinceTracker",
  data() {
    return {
      internTraker: [
        {
          name: "Soji Aminu",
          role: "Senior Digital Product Designer @andela",
          picture: require("../assets/soji.png"),
          about:
            "An exceptional product designer with years of experience understanding the users thinking pattern and this helps in creating user centered product.",
        },
        {
          name: "Soji Aminu",
          role: "Senior Digital Product Designer @andela",
          picture: require("../assets/soji.png"),
          about:
            "An exceptional product designer with years of experience understanding the users thinking pattern and this helps in creating user centered product.",
        },
        {
          name: "Soji Aminu",
          role: "Senior Digital Product Designer @andela",
          picture: require("../assets/soji.png"),
          about:
            "An exceptional product designer with years of experience understanding the users thinking pattern and this helps in creating user centered product.",
        },
        {
          name: "Soji Aminu",
          role: "Senior Digital Product Designer @andela",
          picture: require("../assets/soji.png"),
          about:
            "An exceptional product designer with years of experience understanding the users thinking pattern and this helps in creating user centered product.",
        },
      ],
    };
  },
};
</script>

<style scoped>
.tracker {
  width: 70%;
}
.tracker-jobless {
  margin-left: -2%;
}
</style>