import axios from 'axios'

const pagesStore = {
  state: () => ({
    contact: null
  }),
  mutations: {
    SET_CONTACT_CONTENT: (state, content) => {
      state.contact = content
    },
  },
  actions: {
    async getContactContent({ commit }) {
      let response = await axios.get(process.env.VUE_APP_API_BASE_URL + 'pages/contact')
      commit('SET_CONTACT_CONTENT', response.data.content)
    }
  }
}

export default pagesStore