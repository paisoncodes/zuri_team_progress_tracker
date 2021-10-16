import { createStore } from 'vuex'
import ContributionServices from '@/services/http-client'

export default createStore({
  state: {
    profileModalActive: false,
    intern: [],
    stats20: [],
    stats19: [],
    stats18: []
  },
  mutations: {
    toggleProfileEditModal: state => {
      state.profileModalActive =! state.profileModalActive
    },
    setStack(state, payload) { state.intern = payload },
    setStats20(state, payload) {
      state.stats20 = payload
    },
    setStats19(state, payload) {
      state.stats19 = payload
    },
    setStats18(state, payload) {
      state.stats18 = payload
    }
  },
  actions: {
    async getStack({commit}, payload) {
      await ContributionServices.getStack(payload).then(response => {
        commit("setStack", response.data.data)
        console.log(response.data.data)
      })
    },
    async getTotalSalary() {
      await ContributionServices.getTotalSalary().then(response => {
        console.log(response)
      })
    },
    async getStatistics20({commit}, payload) {
      await ContributionServices.getStatistics(payload).then(res => {
        commit("setStats20", res.data)
      })
    },
    async getStatistics19({commit}, payload) {
      await ContributionServices.getStatistics(payload).then(res => {
        commit("setStats19", res.data)
      })
    },
    async getStatistics18({commit}, payload) {
      await ContributionServices.getStatistics(payload).then(res => {
        commit("setStats18", res.data)
      })
    }
  },
  modules: {
  }
})