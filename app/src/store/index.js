import Vue from 'vue'
import Vuex from 'vuex'

import worksStore from './works'
import pagesStore from './pages'

Vue.use(Vuex)

export default new Vuex.Store({
  rot: true,
  modules: {
    works: worksStore,
    pages: pagesStore
  },
  actions: {
    initialize() {
      this.dispatch('getWorks')
      this.dispatch('getContactContent')
    }
  }
})
