import { createStore } from 'vuex'
import ContributionServices from '@/services/http-client'

export default createStore({
  state: {
    profileModalActive: false,
    intern: [],
    stacks: []
  },
  mutations: {
    toggleProfileEditModal: state => {
      state.profileModalActive =! state.profileModalActive
    },
    setStack(state, payload) { state.intern = payload },
    setStackYear(state, payload) {state.stacks = payload}
  },
  actions: {
    async getStack({commit}, payload) {
      await ContributionServices.getStack(payload).then(response => {
        commit("setStack", response.data.data)
        console.log(response.data.data)
      })
    },
    async getStackYear({commit}, payload) {
      await ContributionServices.getStackYear(payload).then(response => {
        commit("setStackYear", payload)
        console.log(response.data.data)
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
    }
  },
  modules: {
  }
})