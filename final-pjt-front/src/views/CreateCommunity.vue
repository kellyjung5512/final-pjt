<template>
  <div class="container create-community-form" style="position: relative; top: 150px;">
    <div class="">
      <h2 class="text-center">게시글 작성</h2>
      <div class="row">
        <div class="form-group">
          <label for='title'>제목</label>
          <input class="form-control mb-3" id="title" type="text" v-model.trim="title" required='required' placeholder="제목을 입력하시오">
        </div>
        <div class="clearfix"></div>
        <div class="form-group">
          <label for="content">내용</label>
          <textarea class="form-control mb-3" id="content" rows="5" v-model.trim="content" required='required' placeholder="내용을 입력하시오"></textarea>
        </div>
      </div>
      <div class="col-md-12 form-group mb-5">
        <button class="btn btn-success fw-bold" @click="createCommunity">등록</button>
      </div>
    </div>
  </div>    
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateCommunity',
  data: function () {
    return {
      title: '',
      content: '',
    }
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers:{
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    createCommunity: function () {
      const config = this.getToken()
      const communityItem = {
        title: this.title,
        content: this.content,
      }
      axios.post(`${SERVER_URL}/community/`, communityItem, config)
      .then(() => {
        this.$emit('community-created')
        this.title = ""
        this.content = ""
        this.$router.push({ name: 'Community' })
      })
      .catch((err) => {
        console.log(err)
        alert('게시글 작성이 실패했습니다.')
      })
    }
  }

}
</script>

<style>
.post {
  position: relative;
  width: 500px;
  margin: 50px auto 100px auto;
  }
.create-community-form {
  position: relative;
  background-color: rgb(0, 0, 0, 0);
  /* border: solid rgb(255, 255, 255, 0) 1px; */
  border-radius: 4px;
  box-sizing: border-box;
  margin: 20px auto 10px;
}
.create-community-form h2 {
  padding: 10px 10px 1px;
  font-size: 24px;
  font-weight: bold;
  color: white;
  text-transform: uppercase;
}
.create-community-form .form-control {
  border: 0px;
  background: white;
  min-height: 50px;
  outline: none;
  border: solid 2px black;
  /* border-bottom: none; */
}
.create-community-form > .row {
    margin: 0 -1.5%;
}

.create-community-form label {
  float: left;
  display: block;
  margin: 10px 10px 10px;
  color: rgba(255, 255, 255, 0.979);
  font-size: 20px;
  font-weight: bold;
  line-height: 1;
  text-transform: uppercase;
  letter-spacing: .2em;
  
}

.create-community-form input {
  outline: none;
  display: block;
  background: rgba(black, 0.1);
  width: 100%;
  border: 0;
  border-radius: 4px;
  box-sizing: border-box;
  padding: 12px 20px;
  color: gray;
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
  transition: 0.3s ease;
}

.create-community-form textarea {
  outline: none;
  display: block;
  background: rgba(black, 0.1);
  width: 100%;
  border: 0;
  border-radius: 4px;
  box-sizing: border-box;
  padding: 12px 20px;
  color: gray;
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
  transition: 0.3s ease;
}

.create-community-form button {
  outline: none;
  background: linear-gradient(125deg,#586d6d,#4d40b6,#b13e51);
  margin: 10px 0 ;
  width: 100%;
  border: 0;
  border-radius: 4px;
  padding: 12px 20px;
  color: white;
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
  text-transform: uppercase;
  cursor: pointer;
}
</style>