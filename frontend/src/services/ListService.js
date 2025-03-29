import axios from 'axios'
import AuthService from './AuthService'

const API_URL = 'http://127.0.0.1:8000/api/lists/'

export default {
  async getLists(boardId) {
    try {
      const token = AuthService.getAccessToken()
      const response = await axios.get(API_URL, {
        headers: { Authorization: `Bearer ${token}` },
        params: { board: boardId },
      })
      return response.data
    } catch (error) {
      console.error('Error al obtener las listas:', error)
      throw error
    }
  },

  async createList(boardId, name) {
    try {
      const token = AuthService.getAccessToken()
      const response = await axios.post(
        API_URL,
        { name, board: boardId },
        { headers: { Authorization: `Bearer ${token}` } },
      )
      return response.data
    } catch (error) {
      console.error('Error al crear la lista:', error)
      throw error
    }
  },

  async deleteList(listId) {
    try {
      const token = AuthService.getAccessToken()
      await axios.delete(`${API_URL}${listId}/`, {
        headers: { Authorization: `Bearer ${token}` },
      })
    } catch (error) {
      console.error('Error al eliminar la lista:', error)
      throw error
    }
  },
}
