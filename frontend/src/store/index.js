import { createStore } from 'vuex'
import ContributionServices from '@/services/http-client'

export default createStore({
  state: {
    profileModalActive: false,
    intern: [],
    stacks: [],
    year: [],
    allInterns:[],
    internJob:[]
  },
  mutations: {
    toggleProfileEditModal: state => {
      state.profileModalActive =! state.profileModalActive
    },
    setStack(state, payload) { state.intern = payload },
    setStackYear(state, payload) {state.stacks = payload},
    setYear(state, payload) {state.year = payload},
    allInterns(state, payload) { state.allInterns = payload },
    userJob(state, payload) { state.internJob.push(payload) },
  },
  actions: {
    async getAllStack({commit, getters}) {
      const year = getters.year
      await ContributionServices.getAllStack(year).then(response => {
        commit("allInterns", response.data)
        console.log(response.data)
      })
    },
    async getStack({commit, getters}, payload) {
      const year = getters.year
      await ContributionServices.getStack(payload, year).then(response => {
        commit("allInterns", response.data)
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
    }

  },
  getters:{
    allInterns(state){
      return state.allInterns
    },
    allUserjobs (state){
      return state.internJob
    },
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