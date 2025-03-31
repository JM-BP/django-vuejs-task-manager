// src/store.js
import { createStore } from 'vuex'

const store = createStore({
  state() {
    return {
      user: JSON.parse(localStorage.getItem('user')) || null, // Persistir usuario
    }
  },
  mutations: {
    setUser(state, user) {
      state.user = user
      localStorage.setItem('user', JSON.stringify(user)) // Persistir en localStorage
    },
    logout(state) {
      state.user = null
      localStorage.removeItem('user') // Limpiar localStorage
    },
  },
  actions: {
    login({ commit }, user) {
      commit('setUser', user)
    },
    logout({ commit }) {
      commit('logout')
    },
  },
  getters: {
    isAuthenticated(state) {
      return state.user !== null
    },
    getUser(state) {
      return state.user
    },
  },
})

export default store
