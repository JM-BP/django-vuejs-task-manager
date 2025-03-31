import axios from 'axios'
import AuthService from './AuthService'

const API_URL = 'http://127.0.0.1:8000/api/lists/'

export default {
  async getLists(boardId) {
    const token = AuthService.getAccessToken()
    const response = await axios.get(`${API_URL}?board=${boardId}`, {
      headers: { Authorization: `Bearer ${token}` },
    })
    return response.data
  },

  async createList(boardId, name) {
    const token = AuthService.getAccessToken()
    const response = await axios.post(
      API_URL,
      { board: boardId, name },
      { headers: { Authorization: `Bearer ${token}` } },
    )
    return response.data
  },
}
