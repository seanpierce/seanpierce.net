import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    works: []
  },
  mutations: {
    SET_WORKS: (state, works) => {
      state.works = works
    },
  },
  actions: {
    async getWorks({ commit }) {
      let response = await axios.get(process.env.VUE_APP_API_BASE_URL + 'works')
      commit('SET_WORKS', response.data)
    }
  },
  modules: {
  }
})
