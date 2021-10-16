import { createStore } from 'vuex'
import ContributionServices from '@/services/http-client'
import { getField, updateField } from 'vuex-map-fields';

export default createStore({
  state: {
    profileModalActive: false,
    intern: [],
    stats20: [],
    stats19: [],
    stats18: [],
    allInterns:[],
    internJob:[],
    currentUserID:null,
    formOne : {
      fullName : '',
      currentSalary : '',
      about: '',
      employed: '',
      // image: ''
    },
    formTwo:{

    }

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
    },
    allInterns(state, payload) { state.allInterns = payload },
    userJob(state, payload) { state.internJob.push(payload) },
    currentUserId(state, payload){state.currentUserID = payload},

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
        // await ContributionServices.editIntern().then(response => {
        //   console.log(respnose)
        // })
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