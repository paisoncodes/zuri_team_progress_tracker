import { createStore } from 'vuex'
import ContributionServices from '@/services/http-client'
import { getField, updateField } from 'vuex-map-fields';
import Axios from 'axios';

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
    formConfirmation: false

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
      console.log(state.imageOne)
    },
    setImageTwo(state, payload){
      state.imageTwo = payload
      console.log(state.imageTwo)
    }

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
      formData.append('current_salary', state.formOne.currentSalary)
      formData.append('about', state.formOne.about)
      formData.append('is_employed', state.formOne.employed)
      
      formData.append('image', state.imageOne)

    for(var pair of formData.entries()){
        console.log(pair[0], pair[1]);
    } 

      try {
        const response = await Axios.put(`https://zuri-progress-tracker.herokuapp.com/api/v1/interns/${state.currentUserID}/update`, formData, {
    headers: {
      "Content-Type": "multipart/form-data; boundary {}"
    }
    
    })
    console.log(response);
    console.log(response.data)
      } catch (error) {
        console.log(error)
      } finally{
        state.formConfirmation =! state.formConfirmation
      }

    },

    async postJob({state}){
      let formData = new FormData();
      formData.append('job_title', state.formTwo.position)
      formData.append('company_name', state.formTwo.company)
      formData.append('job_description', state.formTwo.about)
      formData.append('gotten_at', state.formTwo.dateGotten)
      formData.append('image', state.imageTwo)

      for(var pair of formData.entries()){
        console.log(pair[0], pair[1]);
    } 

      try {
        const response = await Axios.post(`http://zuri-progress-tracker.herokuapp.com/api/v1/interns/${state.currentUserID}/jobs`, formData, {
    headers: {
      "Content-Type": "multipart/form-data; boundary {}",
      "Access-Control-Allow-Origin": "*"
      
    },
    
    })
    console.log(response);
    console.log(response.data)
      } catch (error) {
        console.log(error)
      }
    },
    async getProgresStat({commit}, payload) {
      await ContributionServices.getProgresStat(payload).then(res => {
        commit("setProgresStat", res.data.sort((a, b) => b.year - a.year ).slice(0,3));
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
  },
  modules: {
  },
})