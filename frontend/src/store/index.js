import { createStore } from 'vuex'
import ContributionServices from '@/services/http-client'
import { getField, updateField } from 'vuex-map-fields';

export default createStore({
  state: {
    profileModalActive: false,
    intern: [],
    totalSalary: '',
    stacks: [],
    year: [],
    stats20: [],
    stats19: [],
    stats18: [],
    allInterns:[],
    internJob:[],
    progresStat:[],
    currentUserID:null,
    formOne : {
      full_name : '',
      currentSalary : '',
      about: '',
      employed: '',
      image: ''
    },
    formTwo:{
      position : '',
      company : '',
      dateGotten: '',
      jobDescription: '',
      image: ''

    }

  },
  mutations: {
    toggleProfileEditModal: state => {
      state.profileModalActive =! state.profileModalActive
    },
    setStack(state, payload) { state.intern = payload },
    setTotalSalary(state, payload) {
      state.totalSalary = payload
    },

    setStackYear(state, payload) {state.stacks = payload},
    setYear(state, payload) {state.year = payload},
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
    setProgresStat(state, payload) {
      state.progresStat = payload
    },

    updateField,
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
    async getTotalSalary({ commit }) {
      await ContributionServices.getTotalSalary().then(response => {
        commit('setTotalSalary', response.data.total_salary)
        console.log(response.data)
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
      let formData = new FormData();
      formData.append('full_name', state.formOne.full_name)
      formData.append('current_Salary', state.formOne.currentSalary)
      formData.append('about', state.formOne.about)
      formData.append('is_employed', state.formOne.employed)

      try {
        await ContributionServices.editIntern(state.currentUserID, formData).then(response => {
          console.log(response)
        })
      } catch (error) {
        console.log(error)
      }
    },

    async postJob({state}){
      let formData = new FormData();
      formData.append('job_title', state.formOne.position)
      formData.append('company_name', state.formOne.company)
      formData.append('job_description', state.formOne.about)
      formData.append('gotten_at', state.formOne.dateGotten)

      try {
        await ContributionServices.postJob(state.currentUserID, formData).then(response => {
          console.log(response)
        })
      } catch (error) {
        console.log(error)
      }
    },
    async getProgresStat({commit}, payload) {
      await ContributionServices.getProgresStat(payload).then(res => {
        commit("setProgresStat", res.data.sort((a, b) => b.year - a.year ).slice(0,3));
        // console.log(res.data);
        console.log(res.data.sort((a, b) => b.year - a.year ).slice(0,3))
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
    progresStat(state){
      return state.progresStat
    },
    getField,
  },
  modules: {
  },
})