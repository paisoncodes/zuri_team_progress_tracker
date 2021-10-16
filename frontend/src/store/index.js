import { createStore } from 'vuex'
import ContributionServices from '@/services/http-client'

export default createStore({
  state: {
    profileModalActive: false
  },
  mutations: {
    toggleProfileEditModal: state => {
      state.profileModalActive =! state.profileModalActive
    },
    
  },
  actions: {
    async getTotalSalary() {
      await ContributionServices.getTotalSalary().then(response => { console.log(response)})
    },
  },
  modules: {
  }
})