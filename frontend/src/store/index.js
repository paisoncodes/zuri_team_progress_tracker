import { createStore } from 'vuex'
import ContributionServices from '@/services/http-client'

export default createStore({
  state: {
    profileModalActive: false,
    intern: [],
    totalSalary: '',
  },
  mutations: {
    toggleProfileEditModal: state => {
      state.profileModalActive =! state.profileModalActive
    },
    setStack(state, payload) { state.intern = payload },
    setTotalSalary(state, payload) {
      state.totalSalary = payload
    }

  },
  actions: {
    async getStack({commit}, payload) {
      await ContributionServices.getStack(payload).then(response => {
        commit("setStack", response.data.data)
        console.log(response.data.data)
      })
    },
    async getTotalSalary({ commit }) {
      await ContributionServices.getTotalSalary().then(response => {
        commit('setTotalSalary', response.data.total_salary)
        console.log(response.data)
      })
    }
  },
  modules: {
  }
})