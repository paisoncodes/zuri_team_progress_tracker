import { createStore } from 'vuex'
import ContributionServices from '@/services/http-client'
import { getField, updateField } from 'vuex-map-fields';

export default createStore({
  state: {
    profileModalActive: false,
    intern: [],
    formOne : {
      fullName : '',
      currentSalary : '',
      about: '',
      employed: '',
      // image: ''
  }
  },
  mutations: {
    toggleProfileEditModal: state => {
      state.profileModalActive =! state.profileModalActive
    },
    setStack(state, payload) { state.intern = payload },
    // setData(state, payload){
    //   state.myData = payload
    // }
    updateField,

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
    async editIntern({state}){
      console.log(state.formOne)
      // await ContributionServices.editIntern().then(response => {
      //   console.log(respnose)
      // })
    },

  },
  modules: {
  },
  getters: {
    getField,
  },
})