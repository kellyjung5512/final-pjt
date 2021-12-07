import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    login: false,
    token: '',
    nextPage : '',
    nextparams: {},
  },
  mutations: {
    LOGIN : function(state, res) {
      const token = res.data.token
      state.token = token
    },
    LOGOUT : function(state) {
      state.token =''
    },
    SETNEXTPAGE : function(state, res) {
      if (res.name) {
        state.nextPage=res.name
      } else {
        state.nextPage=''
        state.nextparams={}
      }      
      if (res.params !={}) { 
        state.nextparams= res.params
      } else {
        state.nextparams={}
      }
    }
  },
  actions: {
    login: function({ commit },res) {
      commit('LOGIN',res)
    },
    logout: function({ commit }, res) {
      commit('LOGOUT',res)
    },
    setNextPage: function({ commit }, res) {
      commit('SETNEXTPAGE', res)
    }
  },
  modules: {
  }
})