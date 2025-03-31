<template>
  <div class="dashboard">
    <h2>Tableros</h2>
    <input v-model="newBoardName" placeholder="Nombre del tablero" />
    <button @click="createBoard">Crear Tablero</button>

    <ul>
      <li v-for="board in boards" :key="board.id" @click="goToBoard(board.id)">
        {{ board.name }}
      </li>
    </ul>
  </div>
</template>

<script>
import BoardService from '../services/BoardService'
import { useRouter } from 'vue-router'

export default {
  data() {
    return {
      newBoardName: '',
      boards: [],
    }
  },
  setup() {
    const router = useRouter()
    return { router }
  },
  methods: {
    async fetchBoards() {
      try {
        this.boards = await BoardService.getBoards()
      } catch (error) {
        console.error('Error al obtener tableros:', error)
      }
    },
    async createBoard() {
      if (!this.newBoardName) return
      try {
        await BoardService.createBoard(this.newBoardName)
        this.newBoardName = ''
        this.fetchBoards()
      } catch (error) {
        console.error('Error al crear tablero:', error)
      }
    },
    goToBoard(boardId) {
      this.router.push(`/board/${boardId}`)
    },
  },
  mounted() {
    this.fetchBoards()
  },
}
</script>

<style scoped>
.dashboard {
  max-width: 600px;
  margin: auto;
  padding: 20px;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  cursor: pointer;
  padding: 10px;
  background: #eee;
  margin-top: 5px;
  border-radius: 5px;
}
li:hover {
  background: #ddd;
}
</style>

<!--
<template>
  <div class="dashboard">
    <h2>Mis Tableros</h2>
    <div class="new-board">
      <input type="text" v-model="newBoardName" placeholder="Nombre del tablero" />
      <button @click="createBoard">Crear</button>
    </div>
    <div v-if="boards.length === 0">No tienes tableros aún.</div>
    <ul class="board-list">
      <li v-for="board in boards" :key="board.id">
        <router-link :to="'/boards/' + board.id">{{ board.name }}</router-link>
        <button @click="deleteBoard(board.id)">🗑</button>
      </li>
    </ul>
  </div>
</template>

<script>
import BoardService from '../services/BoardService'

export default {
  data() {
    return {
      boards: [],
      newBoardName: '',
    }
  },
  async created() {
    await this.fetchBoards()
  },
  methods: {
    async fetchBoards() {
      try {
        this.boards = await BoardService.getBoards()
      } catch (error) {
        console.error('Error al cargar los tableros:', error)
      }
    },
    async createBoard() {
      if (!this.newBoardName) return
      try {
        await BoardService.createBoard(this.newBoardName)
        this.newBoardName = ''
        await this.fetchBoards()
      } catch (error) {
        console.error('Error al crear el tablero:', error)
      }
    },
    async deleteBoard(boardId) {
      try {
        await BoardService.deleteBoard(boardId)
        await this.fetchBoards()
      } catch (error) {
        console.error('Error al eliminar el tablero:', error)
      }
    },
  },
}
</script>

<style scoped>
.dashboard {
  max-width: 600px;
  margin: auto;
  text-align: center;
}
.new-board {
  margin-bottom: 20px;
}
input {
  padding: 5px;
  margin-right: 10px;
}
button {
  padding: 5px 10px;
  cursor: pointer;
}
.board-list {
  list-style: none;
  padding: 0;
}
.board-list li {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  background: #f9f9f9;
  margin-bottom: 5px;
  border-radius: 5px;
}
</style>
-->
