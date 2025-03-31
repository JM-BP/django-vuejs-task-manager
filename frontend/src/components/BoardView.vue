<template>
  <div class="board-view">
    <h2>{{ board.name }}</h2>
    <input v-model="newListName" placeholder="Nombre de la lista" />
    <button @click="createList">Crear Lista</button>

    <div class="lists">
      <div v-for="list in lists" :key="list.id" class="list" :data-list-id="list.id">
        <h3>{{ list.name }}</h3>
        <input v-model="newTaskTitle[list.id]" placeholder="Nueva tarea" />
        <button @click="createTask(list.id)">Añadir Tarea</button>

        <!-- Lista de tareas con funcionalidad de arrastrar y soltar -->
        <draggable
          v-model="list.tasks"
          group="tasks"
          @end="onTaskDrop"
          item-key="id"
          class="task-list"
        >
          <template #item="{ element }">
            <div class="task">{{ element.title }}</div>
          </template>
        </draggable>
      </div>
    </div>
  </div>
</template>

<script>
import BoardService from '../services/BoardService'
import ListService from '../services/ListService'
import TaskService from '../services/TaskService'
import { useRoute } from 'vue-router'
import { ref } from 'vue'
import draggable from 'vuedraggable'

export default {
  components: {
    draggable,
  },
  data() {
    return {
      board: {},
      lists: [],
      newListName: '',
      newTaskTitle: {},
    }
  },
  setup() {
    const route = useRoute()
    return { route }
  },
  methods: {
    async fetchBoard() {
      try {
        this.board = await BoardService.getBoard(this.route.params.id)
      } catch (error) {
        console.error('Error al obtener tablero:', error)
      }
    },
    async fetchLists() {
      try {
        this.lists = await ListService.getLists(this.route.params.id)
      } catch (error) {
        console.error('Error al obtener listas:', error)
      }
    },
    async createList() {
      if (!this.newListName) return
      try {
        await ListService.createList(this.route.params.id, this.newListName)
        this.newListName = ''
        this.fetchLists()
      } catch (error) {
        console.error('Error al crear lista:', error)
      }
    },
    async createTask(listId) {
      if (!this.newTaskTitle[listId]) return
      try {
        await TaskService.createTask(listId, this.newTaskTitle[listId])
        this.newTaskTitle[listId] = ''
        this.fetchLists()
      } catch (error) {
        console.error('Error al crear tarea:', error)
      }
    },
    async onTaskDrop(event) {
      try {
        const taskId = event.item.__draggable_context.element.id
        const newListElement = event.to.closest('.list') // Buscar el elemento HTML de la nueva lista
        if (!newListElement) {
          console.error('No se pudo determinar la nueva lista')
          return
        }

        const newListId = newListElement.getAttribute('data-list-id') // Obtener el ID de la lista destino
        if (!newListId) {
          console.error('ID de lista destino no encontrado')
          return
        }

        await TaskService.updateTask(taskId, { list: newListId })
        console.log('Tarea movida correctamente')

        // Recargar las listas para reflejar los cambios
        await this.fetchLists()
      } catch (error) {
        console.error('Error al mover tarea:', error)
      }
    },
  },
  mounted() {
    this.fetchBoard()
    this.fetchLists()
  },
}
</script>

<style scoped>
.board-view {
  text-align: center;
  max-width: 800px;
  margin: auto;
  padding: 20px;
}
.lists {
  display: flex;
  gap: 20px;
}
.list {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px;
  width: 200px;
}
.task-list {
  min-height: 50px;
  background: #f8f8f8;
  padding: 10px;
  border-radius: 5px;
}
.task {
  padding: 10px;
  margin-bottom: 5px;
  background: #fff;
  border-radius: 5px;
  cursor: grab;
}
.task:active {
  cursor: grabbing;
}
</style>
