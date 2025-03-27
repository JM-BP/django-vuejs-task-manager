<template>
  <div class="login-container">
    <h2>Iniciar Sesión</h2>
    <form @submit.prevent="handleLogin">
      <div>
        <label>Usuario:</label>
        <input type="text" v-model="username" required />
      </div>
      <div>
        <label>Contraseña:</label>
        <input type="password" v-model="password" required />
      </div>
      <button type="submit">Ingresar</button>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script>
import AuthService from '../services/AuthService'
import { useRouter } from 'vue-router'

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: '',
    }
  },
  setup() {
    const router = useRouter()

    return { router }
  },
  methods: {
    async handleLogin() {
      try {
        await AuthService.login(this.username, this.password)
        this.router.push('/dashboard')
      } catch (error) {
        this.errorMessage = 'Credenciales incorrectas'
      }
    },
  },
}
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  text-align: center;
}
.error {
  color: red;
}
</style>
