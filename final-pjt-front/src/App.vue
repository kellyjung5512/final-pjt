<template>
  <div id="app">
    <!-- <div class="column">  -->
    <router-link to="/"><img :src="new_logo" class="popcorn" alt="logo"></router-link>
    <router-view @login="userLogin"/> 
    <Slide right>
      <span v-if="login"><router-link to="/" class="sidemenu">홈</router-link></span>
      <span v-if="login"><router-link :to="{ name: 'Community' }"  class="sidemenu">게시판</router-link></span> 
      <span v-if="login"><router-link to="/search" class="sidemenu">검색</router-link></span>
      <!-- <span v-if="login"><router-link to="/worldcup" class="sidemenu" style="text-decoration: line-through;">월드컵</router-link></span> -->
      <span v-if="login"><router-link :to="{ name: 'Profile' }" class="sidemenu">프로필</router-link></span>
      <span v-if="login"><router-link @click.native="logout" to="#" class="sidemenu">로그아웃</router-link></span>
      <span v-if="!login"><router-link :to="{ name: 'Login' }" class="sidemenu">로그인</router-link></span>
      <span v-if="!login"><router-link :to="{ name: 'Signup' }" class="sidemenu">회원가입</router-link></span>
    </Slide>
    <!-- </div>    -->
  </div>
</template>

<script>
import new_logo from "@/assets/new_logo.png"
import router from '@/router'
import { Slide } from 'vue-burger-menu'

export default {
  name: 'App',
  components: {
    Slide
  },
  props: {
    login_info: Boolean
  },
  data: function () {
    return {
      login: false, 
      isResult: false,
      keyword : '',
      searchQuery: '',    
      result: '',
      searchObj: '',
      new_logo: new_logo,
    }
  },
  methods: {
    userLogin: function () {
      this.login = true
    },
    logout: function() {
      localStorage.removeItem('jwt')
      this.login = false
      this.$router.push({ name: 'Login' })
    },
    getSearch: function () {
      if (this.searchObj !== '') {
        router.push({ name: 'search', params: {name: this.searchObj}})
      }
    },  
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.login = true
    }
  },
}
</script>


<style>
#app {
  font-family:'Raleway','Sunflower', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: start;
  color: lightgray;   
}

#nav {
  padding: 30px;
}

#nav a {
  font-family: 'Abel', sans-serif;
  text-transform: uppercase;
  font-weight: lighter;
  color: lightgray; 
}

#nav a.router-link-exact-active {
  color: #30b34cc7;
}

#nc-main {
  position: relative;
  height: 100vh;
  overflow-x: hidden;
  -webkit-box-shadow: 0 0 30px #241d20;
  box-shadow: 0 0 30px #241d20;
  -webkit-transition: -webkit-transform 0.4s;
  transition: -webkit-transform 0.4s;
  transition: transform 0.4s;
  transition: transform 0.4s, -webkit-transform 0.4s;
}

.column {
  height: 90px;
  float: left;
  width: 100%;
  position: relative;
  z-index:100000;
}

.bm-menu {
  height: 100%; /* 100% Full-height */
  width: 0; /* 0 width - change this with JavaScript */
  position: fixed; /* Stay in place */
  z-index: 1000; /* Stay on top */
  top: 0;
  left: 0;
  background-color: rgba(2, 1, 1, 0.8); /* Black*/
  overflow-x: hidden; /* Disable horizontal scroll */
  padding-top: 60px; /* Place content 60px from the top */
  transition: 0.5s; /*0.5 second transition effect to slide in the sidenav*/
}
.bm-burger-button {
  position: fixed;
  width: 25px;
  height: 20px;
  left: 36px;
  top: 36px;
  cursor: pointer;
}
.sidemenu {
  color: lightgray; 
  font-size: 15px; 
  text-decoration: none;
}
.popcorn {
  position: fixed;
  width: 120px;
  margin-top: 20px;
  margin-left: 20px;
  z-index: 10000;
}
.cross-style {
  position: absolute;
  top: 22px;
  right: 2px;
  cursor: pointer;
}
.bm-cross {
  background: #bdc3c7;
}
.bm-cross-button {
  height: 15px;
  width: 15px;
}
</style>
