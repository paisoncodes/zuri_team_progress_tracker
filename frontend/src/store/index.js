import { createStore } from 'vuex'
import ContributionServices from '@/services/http-client'

export default createStore({
  state: {
    profileModalActive: false,
    intern: [],
    stacks: [],
    year: []
  },
  mutations: {
    toggleProfileEditModal: state => {
      state.profileModalActive =! state.profileModalActive
    },
    setStack(state, payload) { state.intern = payload },
    setStackYear(state, payload) {state.stacks = payload},
    setYear(state, payload) {state.year = payload},
  },
  actions: {
    async getAllStack({commit, getters}) {
      const year = getters.year
      await ContributionServices.getAllStack(year).then(response => {
        commit("setStack", response.data.data)
        console.log(response.data)
      })
    },
    async getStack({commit, getters}, payload) {
      const year = getters.year
      await ContributionServices.getStack(payload, year).then(response => {
        commit("setStack", response.data.data)
        console.log(response.data)
      })
    },
    async getYear({commit}, payload) {
      commit("setYear", payload)
    },
    async getStackYear({commit}, payload) {
      await ContributionServices.getStackYear(payload).then(response => {
        commit("setStackYear", response.data.stacks)
        console.log(response.data.stacks)
      })
    },
    async getTotalSalary() {
      await ContributionServices.getTotalSalary().then(response => {
        console.log(response)
      })
    }
  },
  getters: {
    stacks(state) {
      return state.stacks
    },
    year(state) {
      return state.year
    }
  },
  modules: {
  }
})