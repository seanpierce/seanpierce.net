import axios from 'axios'

const worksStore = {
  state: () => ({
    works: []
  }),
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
  getters: {
    getWorkBySlug: (state) => (slug) => {
      return state.works.find(x => x.slug.toLowerCase() === slug.toLowerCase())
    }
  }
}

export default worksStore