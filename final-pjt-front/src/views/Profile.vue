<template>
  <div id="app container">
    <div style="padding: 100px 70px 50px 70px">
      <div style="padding:10px; margin-right:10px;">
        <h2 class="text-start" ><i class="far fa-smile-wink"></i> 어서오세요, {{ user.username }}님!</h2>
      </div>
      <hr>
      <img :src="likemovielist1" alt="" class="d-flex justify-content-flex-start" style="padding-bottom: 1px">
      <vue-glide v-if="my_like_movies.length"
        class="glide__track"
        data-glide-el="track"
        ref="slider"
        type="carousel"
        :breakpoints="{3000: {perView: 5}, 1500: {perView: 3}, 945: {perView: 2}, 542: {perView: 1}}"
      >
        <vue-glide-slide v-for="(movie, idx) in my_like_movies" :key="idx">        
          <MovieCard :movie="movie"/>
        </vue-glide-slide>
      </vue-glide>
      <hr>      
  
      <div class="align-item:center">
        <img :src="writtenarticle" alt="" class="d-flex justify-content-flex-start" style="padding-bottom: 2px">
          <div v-for="(community, idx) in communities" :key="idx"> 
            <span v-if="user.username === community.auth_user">
              <span 
                @click="communityDetail(community)" 
                style="margin-left:10px; padding-bottom: 10px;">
                <i class="far fa-sticky-note"></i> 
                {{ community.title }} - {{ community.created_at|MMdd }}
              </span>
            </span>
          </div>
      </div>
      <br>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { Glide, GlideSlide } from 'vue-glide-js'
import MovieCard from "@/components/MovieCard"
import VueJwtDecode from "vue-jwt-decode"
import likemovielist1 from "@/assets/images/likemovielist1.png"
import writtenarticle from "@/assets/images/writtenarticle.png"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "MyProfile",
  data: function () {
    return { 
      like_movies: [],
      my_like_movies: [],
      communities: [],
      comments: [],
      user: '',
      likeMovieCount: '',
      likemovielist1,
      writtenarticle,
      name: '',
    }
  },
  components: {
    MovieCard,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide,
    
  },
  computed:{
      movieImage: function () {
        return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}` 
       },
    },

  methods: {
     communityDetail: function (community) {
      this.$router.push({ name: 'CommunityDetail', params: { community_pk: `${community.id}`}})
    },
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },
    getMyProfile: function () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/profile/`, info, config)
      .then((res) => {
        this.user = res.data
        this.like_movies = res.data.like_movies
      })
    },
    getMovieData: function () {
      axios.get(`${SERVER_URL}/movies/`)
      .then((res) => {
        for(let i = 0; i < this.like_movies.length; i++){
          this.my_like_movies.push(res.data[0][this.like_movies[i]-1])
        }
        console.log(this.my_like_movies)
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getCommunity: function () {
    const config = this.getToken()
    const hash = localStorage.getItem('jwt')
    const info = VueJwtDecode.decode(hash)
    axios.post(`${SERVER_URL}/accounts/profile/`, info, config)      
    .then((res) => {
      this.user = res.data        
      axios.get(`${SERVER_URL}/community/`, config)        
      .then((res) => {          
        this.communities = res.data   
        })
      })
      .catch((err) => {
        console.log(err)
      })
    },

  },   

  created: function () {
    this.getMyProfile()
    this.getMovieData()
    this.getCommunity()
    this.likemovies()
   
  },
  filters : {  
    MMdd : function(value){ 
      if(value == '') return '';
      let js_date = new Date(value);
      let year = js_date.getFullYear();
      let month = js_date.getMonth() + 1;
      let day = js_date.getDate();
      let hours = js_date.getHours();
      let minutes = js_date.getMinutes();
      if(month < 10){
        month = '0' + month;
      }
      if(day < 10){
        day = '0' + day;
      }
      if(hours < 10){
        hours = '0' + hours;
      }
      if(minutes < 10){
        minutes = '0' + minutes;
      }
      return year + '-' + month + '-' + day + ' ' + hours + ':' + minutes;
    }
  }
}
</script>

<style>
.profile-title { 
  font-family: 'Dongle', sans-serif;
}
</style>