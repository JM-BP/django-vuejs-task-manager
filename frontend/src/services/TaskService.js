import axios from 'axios'
import AuthService from './AuthService'

const API_URL = 'http://127.0.0.1:8000/api/tasks/'

export default {
  async getTasks(listId) {
    try {
      const token = AuthService.getAccessToken()
      const response = await axios.get(API_URL, {
        headers: { Authorization: `Bearer ${token}` },
        params: { list: listId },
      })
      return response.data
    } catch (error) {
      console.error('Error al obtener tareas:', error)
      throw error
    }
  },

  async createTask(listId, title) {
    try {
      const token = AuthService.getAccessToken()
      const response = await axios.post(
        API_URL,
        { list: listId, title, description: '', completed: false },
        { headers: { Authorization: `Bearer ${token}` } },
      )
      return response.data
    } catch (error) {
      console.error('Error al crear tarea:', error.response?.data || error)
      throw error
    }
  },

  async updateTask(taskId, updates) {
    try {
      const token = AuthService.getAccessToken()
      const response = await axios.patch(`${API_URL}${taskId}/`, updates, {
        headers: { Authorization: `Bearer ${token}` },
      })
      return response.data
    } catch (error) {
      console.error('Error al actualizar tarea:', error)
      throw error
    }
  },

  async deleteTask(taskId) {
    try {
      const token = AuthService.getAccessToken()
      await axios.delete(`${API_URL}${taskId}/`, {
        headers: { Authorization: `Bearer ${token}` },
      })
    } catch (error) {
      console.error('Error al eliminar tarea:', error)
      throw error
    }
  },
}
