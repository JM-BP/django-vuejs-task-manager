<template>
  <div class="board-view">
    <h2>{{ board.name }}</h2>
    <div class="new-list">
      <input type="text" v-model="newListName" placeholder="Nombre de la lista" />
      <button @click="createList">Añadir Lista</button>
    </div>
    <div v-if="lists.length === 0">No hay listas en este tablero.</div>
    <div class="lists">
      <div v-for="list in lists" :key="list.id" class="list">
        <h3>{{ list.name }}</h3>
        <TaskView :listId="list.id" />
      </div>
    </div>
  </div>
</template>

<script>
import ListService from '../services/ListService'
import TaskView from './TaskView.vue'

export default {
  props: ['id'],
  components: { TaskView },
  data() {
    return {
      board: { id: this.id, name: '' },
      lists: [],
      newListName: '',
    }
  },
  async created() {
    await this.fetchLists()
  },
  methods: {
    async fetchLists() {
      try {
        this.lists = await ListService.getLists(this.id)
      } catch (error) {
        console.error('Error al cargar listas:', error)
      }
    },
    async createList() {
      if (!this.newListName) return
      try {
        await ListService.createList(this.id, this.newListName)
        this.newListName = ''
        await this.fetchLists()
      } catch (error) {
        console.error('Error al crear lista:', error)
      }
    },
  },
}
</script>

<style scoped>
.board-view {
  max-width: 800px;
  margin: auto;
  text-align: center;
}
.new-list {
  margin-bottom: 20px;
}
.lists {
  display: flex;
  gap: 20px;
  overflow-x: auto;
}
.list {
  background: #f9f9f9;
  padding: 10px;
  border-radius: 5px;
  min-width: 200px;
}
</style>
