import { createStore } from 'vuex'
import ContributionServices from '@/services/http-client'
import { getField, updateField } from 'vuex-map-fields';

export default createStore({
  state: {
    profileModalActive: false,
    intern: [],
    allInterns:[],
    internJob:[],
    formOne : {
      fullName : '',
      currentSalary : '',
      about: '',
      employed: '',
      // image: ''
    },
    formTwo:{
      position : '',
      company : '',
      dateGotten: '',
      jobDescription: '',
      // image: ''

    }

  },
  mutations: {
    toggleProfileEditModal: state => {
      state.profileModalActive =! state.profileModalActive
    },
    setStack(state, payload) { state.intern = payload },
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
        response
        // console.log(response)
      }) 
    },
    async getAllInterns({commit}){
      await ContributionServices.getIntern().then(response =>{
        commit('allInterns', response.data)
      })
    },

    async getUserJob({commit}, user_id){
           await ContributionServices.getJobs(user_id).then(response => {
             console.log(response)
             commit ('userJob', response.data)
      }).catch((error)=>{
        console.log(error)
      })
    },
    
    async editIntern({state}){
        console.log(state.formOne)
        await ContributionServices.editIntern().then(response => {
          console.log(respnose)
        })
      },

      async postJob({state}){
        console.log(state.formTwo)
        await ContributionServices.postJob().then(response => {
          console.log(respnose)
        })
      },

  },
  getters:{
    allInterns(state){
      return state.allInterns
    },
    allUserjobs (state){
      return state.internJob
    },
    getField,
  },
  modules: {
  },
})