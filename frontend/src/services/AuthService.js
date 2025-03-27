import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/api/token/'

export default {
  async login(username, password) {
    try {
      const response = await axios.post(API_URL, { username, password })
      localStorage.setItem('access', response.data.access)
      localStorage.setItem('refresh', response.data.refresh)
      return response.data
    } catch (error) {
      throw error.response.data
    }
  },

  logout() {
    localStorage.removeItem('access')
    localStorage.removeItem('refresh')
  },

  getAccessToken() {
    return localStorage.getItem('access')
  },

  async refreshToken() {
    try {
      const refresh = localStorage.getItem('refresh')
      if (!refresh) throw new Error('No refresh token available')

      const response = await axios.post(`${API_URL}refresh/`, { refresh })
      localStorage.setItem('access', response.data.access)
      return response.data.access
    } catch (error) {
      this.logout()
      throw error
    }
  },
}
