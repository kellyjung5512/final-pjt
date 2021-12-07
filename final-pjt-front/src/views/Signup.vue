<template>
  <div class="signup-form">
    <h2>회원가입</h2>
    <div class="m-3">
    <div>
      <div class="txtb">
        <div class="form-group">
          <label for="username"></label>
          <input
          type="text" 
          id="username"
          placeholder="아이디 (Username)" 
          required="required"
          v-model.trim="credentials.username"
          >
        </div>
      </div>
    </div>
      <div>
        <div class="txtb">
          <div class="form-group">
            <label for="email"></label>
            <input
            type="email" 
            id="email"
            placeholder="이메일 (example@gmail.com)" 
            required="required"
            v-model.trim="credentials.email"
            >
          </div>
        </div>

      </div>
    <div>
      <div class="txtb">
        <div class="form-group">
          <label for="password"></label>
          <input
          type="password" 
          id="password"
          placeholder="비밀번호 (8자 이상)" 
          required="required"
          v-model.trim="credentials.password">
        </div>
      </div>

    </div>
    <div>
      <div class="txtb">
        <div class="form-group">
          <label for="passwordConfirmation"></label>
          <input
          type="password" 
          id="passwordConfirmation"
          placeholder="비밀번호 확인" 
          required="required"
          v-model.trim="credentials.passwordConfirmation"
          @keypress.enter="signup(credentials)"
          >
        </div>
      </div>
    </div>
    <button
      @click="signup(credentials)" 
      type="submit" 
      class="btn mt-1">회원가입</button>
    <div class="bottom-text">이미 회원이십니까?
      <router-link :to="{ name: 'Login' }" class="ms-1">로그인</router-link>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
        email:'',
      }
    }
  },
  methods: {
    signup: function () {
      axios.post(`${SERVER_URL}/accounts/signup/`, this.credentials)
      .then(() => {
        axios({
          method: 'post',
          url: `${SERVER_URL}/accounts/api-token-auth/`,
          data: this.credentials,
        })
        .then((res) => {
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'Home' })
        })
        .catch((err) => {
          console.log(err)
        })        
      //   this.$router.push({ name: 'Login' })
      })
      .catch((err) => {
        console.log(err)
        alert('회원가입이 실패했습니다.')
      })
    }
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

	body {
		color: #fff;
		background: #19aa8d;
		font-family: 'Roboto', sans-serif;
	}
	.form-control, .form-control:focus, .input-group-addon {
		border-color: #e1e1e1;
	}

	.signup-form {
    width: 500px;
    height: 450px;
    background-color: rgba(0, 0, 0, 0);
    padding: 50px 50px;
    border-radius: 10px;
    position: absolute;
    left: 50%;
    top: 400px;
    transform: translate(-50%,-50%);
	}

	.signup-form h2 {
    text-align: center;
    font-weight: bold;
    padding-bottom: 10px;
    color: white;
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
    padding: 0 2px;
    height: 30px;
}

.form-group {
  margin-bottom: 10px;
}

.btn {
  position:relative;
  left: 50%;
  transform: translateX(-50%);
  margin-bottom: 10px;
  width:95%;
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
.bottom-text{
  margin-top: 10px;
  text-align: center;
  font-size: 15px;
  color: white;
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