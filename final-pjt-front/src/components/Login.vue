<template>
  <div class="login-form">
    <h2>로그인</h2>
    <div class="m-3">
      <div class="txtb">
        <div class="form-group">
          <label for="username"></label>
          <input type="text" id="username" placeholder="아이디 (Username)" v-model.trim="credentials.username">
        </div>
      </div>
      <div class="txtb">
        <div class="form-group">
          <label for="password"></label>      
          <input
          type="password"
          id="password"
          placeholder="비밀번호"
          @keypress.enter="login(credentials)"
          v-model.trim="credentials.password"
          >
        </div>
      </div>
    </div>
    <button @click="login(credentials)" class="btn">로그인</button>
    <div class="bottom-text">
      아직 회원이 아니십니까? 
      <router-link :to="{ name: 'Signup' }" class="ms-1">회원가입</router-link>      
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    login: function () {
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
      .then((res) => {
        console.log(res)
        localStorage.setItem('jwt', res.data.token)
        this.$emit('login') 
        this.$router.push({ name: 'Home' })
      })
      .catch((err) => {
        console.log(err)
        alert('회원정보가 일치하지 않습니다.')
      })
    },


  }
}
</script>
<style scoped>
* {
    margin: 0;
    padding: 0;
    text-decoration: none;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
}
body{
    min-height: 100vh;
}
.login-form{
    width: 500px;
    height: 400px;
    background-color: rgba(0, 0, 0, 0);
    padding: 50px 50px;
    border-radius: 10px;
    position: absolute;
    left: 50%;
    top: 430px;
    transform: translate(-50%,-50%);
}
.login-form h2{
    padding-top: 20px;
    text-align: center;
    font-weight: bold;
    padding-bottom: 10px;
    color:white
}
.txtb{
    border-bottom: 2px solid #adadad;
    position: relative;
    margin: 10px 0;
} 
.txtb input{
    font-size: 15px;
    color: white;
    width: 100%;
    outline: none;
    border: none;
    background: none;
    padding: 0 5px;
    height: 30px;
}

.form-group {
  margin-bottom: 10px;
}

.bottom-text{
    margin-top: 10px;
    text-align: center;
    font-size: 15px;
    color: white;
}

.btn {
  position:relative;
  left: 50%;
  transform: translateX(-50%);
  margin-bottom: 10px;
  width:90%;
  height:40px;
  background: linear-gradient(125deg,#586d6d,#4d40b6,#b13e51) !important;
  background-position: left;
  background-size: 200%;
  color:white;
  font-weight: bold;
  border:none;
  cursor:pointer;
  transition: 0.4s;
  display:inline;
}

::placeholder {
  color: white;
  font-size: 14px;
  font-weight: 100%;
  display: flex;
  text-align: start;
  opacity: 1; 
}

</style>