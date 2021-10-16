import { createStore } from 'vuex'
import ContributionServices from '@/services/http-client'
import { getField, updateField } from 'vuex-map-fields';

export default createStore({
  state: {
    profileModalActive: false,
    intern: [],
    stacks: [],
    year: [],
    stats20: [],
    stats19: [],
    stats18: [],
    allInterns:[],
    internJob:[],
    currentUserID:null,
    formOne : {
      full_name : '',
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
    setStackYear(state, payload) {state.stacks = payload},
    setYear(state, payload) {state.year = payload},
    allInterns(state, payload) { state.allInterns = payload },
    userJob(state, payload) { state.internJob.push(payload) },
    setStats20(state, payload) {
      state.stats20 = payload
    },
    setStats19(state, payload) {
      state.stats19 = payload
    },
    setStats18(state, payload) {
      state.stats18 = payload
    },
<<<<<<< HEAD
=======
    allInterns(state, payload) { state.allInterns = payload },
    userJob(state, payload) { state.internJob.push(payload) },
    currentUserId(state, payload){state.currentUserID = payload},
>>>>>>> 7017dea542dc0f95e7a3bbffea91e81e6fb84ba0

    updateField,
  },
  actions: {
<<<<<<< HEAD
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
=======
    
    async getStack({commit}, payload) {
      await ContributionServices.getStack(payload).then(response => {
        commit("setStack", response.data.data)
        console.log(response.data.data)
>>>>>>> 7017dea542dc0f95e7a3bbffea91e81e6fb84ba0
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
    },
    
    async editIntern({state}){
        console.log(state.formOne)
        await ContributionServices.editIntern().then(response => {
          console.log(response)
        })
      },

      async postJob({state}){
        console.log(state.formTwo)
        await ContributionServices.postJob().then(response => {
          console.log(response)
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
    stacks(state) {
      return state.stacks
    },
    year(state) {
      return state.year
    },
    getField,
  },
  modules: {
  },
})