import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    uid: '',
    accessToken: null,
    titleid : "",
    sectionid : "",
    contentid : "",
    titleList : [],
  },
  getters:{
    getUID: state => state.uid,
    getToken : state => state.accessToken,
    getTitleList : state => state.titleList,
  },
  mutations: {
    LOGIN(state, { id, accessToken }) {
      state.uid = id
      state.accessToken = accessToken
      sessionStorage.uid = id
      sessionStorage.accessToken = accessToken
    },
    LOGOUT(state) {
      state.uid = ""
      state.accessToken = null

      delete sessionStorage.uid
      delete sessionStorage.accessToken
      delete sessionStorage.titleid
      delete sessionStorage.sectionid
      delete sessionStorage.contendid
    },
    selectedTitle(state, titleid){
      state.titleid = titleid
      sessionStorage.titleid = titleid
    },
    selectedSection(state, sectionid){
      state.sectionid = sectionid
      sessionStorage.sectionid = sectionid
    },
    selectedContent(state, contentid){
      state.contentid = contentid
      sessionStorage.contentid = contentid
    },
    updateTitleList(state, titleList){
      state.titleList = titleList
    }
  },
  actions: {
    LOGIN({ commit }, { id, pwd }) {
      return new Promise((resolve, reject) => {
        axios.post('http://110.11.72.247:20000/session/create-session/', {
          memberid: id, memberpwd: pwd
        }).then(res => {
          if (res.data[0].token == "Not Matched") {
            reject("Not Matched")
          }
          else {
            commit('LOGIN', {
              id: id,
              accessToken: res.data[0].token
            })
            resolve()
          }
        })
      })

    },
    LOGOUT({ commit }) {
      commit('LOGOUT')
    }
  }
})
