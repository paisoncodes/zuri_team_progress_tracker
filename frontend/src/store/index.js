import { createStore } from 'vuex'
import ContributionServices from '@/services/http-client'

export default createStore({
  state: {
    profileModalActive: false,
    intern: [],
    allInterns:[],
    internJob:[],
    currentUserID:null
  },
  mutations: {
    toggleProfileEditModal: state => {
      state.profileModalActive =! state.profileModalActive
    },
    setStack(state, payload) { state.intern = payload },
    allInterns(state, payload) { state.allInterns = payload },
    userJob(state, payload) { state.internJob.push(payload) },
      currentUserId(state, payload){state.currentUserID = payload
      console.log(state.currentUserID)
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

  },
  getters:{
    allInterns(state){
      return state.allInterns
    },
    allUserjobs (state){
      return state.internJob
    }
  },
  modules: {
  }
})