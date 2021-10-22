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
    },
    imageOne: '',
    imageTwo: '',
    formTwo:{
      position : '',
      company : '',
      dateGotten: '',
      jobDescription: '',
      image: ''
    },
    formOneConfirmation: false,
    formTwoConfirmation: false,
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
    setImageOne(state, payload){
      state.imageOne = payload
    },
    setImageTwo(state, payload){
      state.imageTwo = payload
    },
  },
  actions: {
    async getAllStack({commit, getters}) {
      const year = getters.year
      await ContributionServices.getAllStack(year).then(response => {
        commit("allInterns", response.data)
      })
    },
    async getStack({commit, getters}, payload) {
      const year = getters.year
      await ContributionServices.getStack(payload, year).then(response => {
        commit("allInterns", response.data)
      })
    },
    async getYear({commit}, payload) {
      commit("setYear", payload)
    },
    async getStackYear({commit}, payload) {
      await ContributionServices.getStackYear(payload).then(response => {
        commit("setStackYear", response.data.stacks)
      })
    },
    async getTotalSalary({ commit }) {
      await ContributionServices.getTotalSalary().then(response => {
        commit('setTotalSalary', response.data.total_salary)
      })
    },
    async getAllInterns({commit}){
      await ContributionServices.getIntern().then(response =>{
        commit('allInterns', response.data)
      })
    },
    async getUserJob({commit}, user_id){
      await ContributionServices.getJobs(user_id).then(response => {
        commit ('userJob', response.data)
      }).catch((error)=>{
        console.log(error)
      })
    },
    async editIntern({state}) {

      try {
        let formData = new FormData();
        formData.append('full_name', state.formOne.full_name)
        formData.append('current_salary', state.formOne.currentSalary)
        formData.append('about', state.formOne.about)
        formData.append('is_employed', state.formOne.employed)
        formData.append('image', state.imageOne)     
      await ContributionServices.editIntern(state.currentUserID, formData).then(res => {
        return res
      })
      } catch (error) {
        console.log(error)
      }finally{
        state.formOneConfirmation = !state.formOneConfirmation
      }
    },
    async postJob({state}) {
      try {
      let formData = new FormData();
      formData.append('job_title', state.formTwo.position)
      formData.append('company_name', state.formTwo.company)
      formData.append('job_description', state.formTwo.about)
      formData.append('gotten_at', state.formTwo.dateGotten)
      formData.append('image', state.imageTwo)

      await ContributionServices.postJob(state.currentUserID, formData).then(res => {
        console.log(res)
      })
      } catch (error) {
        console.log(error)
      }
      finally{
        state.formTwoConfirmation = !state.formTwoConfirmation
      }
    },
    async getProgresStat({commit}, payload) {
      await ContributionServices.getProgresStat(payload).then(res => {
        commit("setProgresStat", res.data.sort((a, b) => b.year - a.year ).slice(0,4));
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
    progresStat(state){
      return state.progresStat
    },
    getField,
    yearParticipants(state){
      const yearParticipants =  state.progresStat.map(item=> {
        return item.participants
      })
      return yearParticipants;
    }
  },
  modules: {
  },
})