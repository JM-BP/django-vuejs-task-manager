import axios from 'axios'
import AuthService from './AuthService'

const API_URL = 'http://127.0.0.1:8000/api/boards/'

const BoardService = {
  async getBoards() {
    try {
      const token = AuthService.getAccessToken()
      const response = await axios.get(API_URL, {
        headers: { Authorization: `Bearer ${token}` },
      })
      return response.data
    } catch (error) {
      console.error('Error al obtener tableros:', error)
      throw error
    }
  },

  async createBoard(name) {
    const token = localStorage.getItem('access')
    if (!token) {
      throw new Error('No hay token disponible')
    }

    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/api/boards/',
        { name },
        {
          headers: { Authorization: `Bearer ${token}` },
        },
      )
      return response.data
    } catch (error) {
      console.error('Error al crear tablero:', error.response ? error.response.data : error)
      throw error
    }
  },

  async deleteBoard(boardId) {
    try {
      const token = AuthService.getAccessToken()
      await axios.delete(`${API_URL}${boardId}/`, {
        headers: { Authorization: `Bearer ${token}` },
      })
    } catch (error) {
      console.error('Error al eliminar tablero:', error)
      throw error
    }
  },
}

export default BoardService
