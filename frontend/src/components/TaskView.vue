<template>
  <div class="task-view">
    <h4>Tareas</h4>
    <div class="new-task">
      <input type="text" v-model="newTaskTitle" placeholder="Nueva tarea" />
      <button @click="createTask">Añadir</button>
    </div>
    <ul v-if="tasks.length > 0">
      <li v-for="task in tasks" :key="task.id">
        <span :class="{ completed: task.completed }">{{ task.title }}</span>
        <button @click="toggleComplete(task)">✔</button>
        <button @click="deleteTask(task.id)">🗑</button>
      </li>
    </ul>
    <p v-else>No hay tareas.</p>
  </div>
</template>

<script>
import TaskService from '../services/TaskService'

export default {
  props: ['listId'],
  data() {
    return {
      tasks: [],
      newTaskTitle: '',
    }
  },
  async created() {
    await this.fetchTasks()
  },
  methods: {
    async fetchTasks() {
      try {
        this.tasks = await TaskService.getTasks(this.listId)
      } catch (error) {
        console.error('Error al cargar tareas:', error)
      }
    },
    async createTask() {
      if (!this.newTaskTitle) return
      try {
        await TaskService.createTask(this.listId, this.newTaskTitle)
        this.newTaskTitle = ''
        await this.fetchTasks()
      } catch (error) {
        console.error('Error al crear tarea:', error)
      }
    },
    async toggleComplete(task) {
      try {
        await TaskService.updateTask(task.id, { completed: !task.completed })
        await this.fetchTasks()
      } catch (error) {
        console.error('Error al actualizar tarea:', error)
      }
    },
    async deleteTask(taskId) {
      try {
        await TaskService.deleteTask(taskId)
        await this.fetchTasks()
      } catch (error) {
        console.error('Error al eliminar tarea:', error)
      }
    },
  },
}
</script>

<style scoped>
.task-view {
  margin-top: 10px;
}
.new-task {
  margin-bottom: 10px;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  display: flex;
  justify-content: space-between;
  padding: 5px;
  background: #f9f9f9;
  margin-bottom: 5px;
  border-radius: 3px;
}
.completed {
  text-decoration: line-through;
  color: gray;
}
</style>
