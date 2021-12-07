<template>
  <div id="app">
    <div style="padding: 100px 70px 50px 70px">
    <br>
    <img :src="random" alt="" class="random">    
    <vue-glide v-if="movies.length"
      class="glide__track m-5"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 5}, 1500: {perView: 3}, 945: {perView: 2}, 542: {perView: 1}}"
    >
      <vue-glide-slide v-for="(movie, idx) in movies" :key="idx">        
        <MovieCard :movie="movie"/>        
      </vue-glide-slide>
    </vue-glide>

    <img :src="popularmovie" alt="" class="popularmovie">
    <div v-if="popular_movies.length === 30"></div>
    <vue-glide v-if="popular_movies.length"
      class="glide__track m-5"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 5}, 1500: {perView: 3}, 945: {perView: 2}, 542: {perView: 1}}"
    >
      <vue-glide-slide v-for="(movie, idx) in popular_movies" :key="idx">        
        <MovieCard :movie="movie"/>        
      </vue-glide-slide>
    </vue-glide>

    <img :src="recentlymovie" alt="" class="recentlymovie">
    <div v-if="latest_movies.length === 30"></div>
    <vue-glide v-if="latest_movies.length"
      class="glide__track m-5"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 5}, 1500: {perView: 3}, 945: {perView: 2}, 542: {perView: 1}}"
    >
      <vue-glide-slide v-for="(movie, idx) in latest_movies" :key="idx">        
        <MovieCard :movie="movie"/>        
      </vue-glide-slide>
    </vue-glide>
    
    <img :src="reco" alt="" class="reco">
    <div v-if="interest_movies.length === 30"></div>
    <vue-glide v-if="interest_movies.length"
      class="glide__track m-5"
      data-glide-el="track"
      ref="slider"
      type="carousel"
      :breakpoints="{3000: {perView: 5}, 1500: {perView: 3}, 945: {perView: 2}, 542: {perView: 1}}"
    >
      <vue-glide-slide v-for="(movie, idx) in interest_movies" :key="idx">
        <MovieCard :movie="movie"/>        
      </vue-glide-slide>
    </vue-glide>
    
    </div>  
  </div>
</template>

<script>
import MovieCard from "@/components/MovieCard"
import random from "@/assets/images/random.png"
import popularmovie from "@/assets/images/popularmovie.png"
import recentlymovie from "@/assets/images/recentlymovie.png"
import reco from "@/assets/images/reco.png"
import { Glide, GlideSlide } from 'vue-glide-js'
import VueJwtDecode from "vue-jwt-decode"
import axios from 'axios'
import _ from 'lodash'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "Home",
  data: function () {
    return {
      user: '',
      movie: '',
      popular_movie: '',
      interest_movie: '',
      movies: [],
      popular_movies: [],
      interest_movies: [],
      latest_movies: [],
      my_favorite_movies: [],
      random,
      popularmovie,
      recentlymovie,
      reco,
    }
  },
  
  components: {
    MovieCard,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide,
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },
    getMovieDatas: function () {
      axios({
        url: `${SERVER_URL}/movies/`,
        method: 'get',
      })      
      .then((res) => {
        console.log(res)
        const randomIdx = _.random(res.data[0].length-1)
        const randomIdx2 = _.random(res.data[1].length-1)
        const randomIdx3 = _.random(res.data[3].length-1)
        this.movie = res.data[0][randomIdx]
        this.popular_movie = res.data[1][randomIdx2]
        this.latest_movies = res.data[2]
        this.interest_movie = res.data[3][randomIdx3]

        const numbers = _.range(1, res.data[0].length);
        const numbers2 = _.range(1, res.data[1].length);
        const numbers3 = _.range(1, res.data[3].length);
        const sampleNums = _.sampleSize(numbers, 30);
        const sampleNums2 = _.sampleSize(numbers2, 30);
        const sampleNums3 = _.sampleSize(numbers3, 30);
        
        for (const key in sampleNums) {
          this.movies.push(res.data[0][sampleNums[key]])
        }
        for (const key in sampleNums2) {
          this.popular_movies.push(res.data[1][sampleNums2[key]])
        }
        for (const key in sampleNums3) {
          this.interest_movies.push(res.data[3][sampleNums3[key]])
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },    
    getRecommend: function () {
      const config = this.getToken()
      const item = {
        movies: this.user.like_movies,
      }
      axios.post(`${SERVER_URL}/movies/${this.user.id}/like/users/`,item ,config)
        .then((res) => {
          const item = {
            users: res.data
          }        
        axios.post(`${SERVER_URL}/accounts/info/`, item, config)
          .then((res) => {
            this.my_favorite_movies = res.data[0]
            })
          .catch((err) => {
            console.log(err)
          })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getMyProfile: function () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`${SERVER_URL}/accounts/profile/`, info, config)
      .then((res) => {
        this.user = res.data
        this.getRecommend()
      })
    },    
  },
  created: function () {
    this.getMovieDatas()
    this.getMyProfile()
   
  },
}
</script>

<style scoped>  
.home-text {
  color: white;
  font-family: 'Noto Sans KR', sans-serif;
}
.random {
  position: absolute;
}

.popularmovie {
  position: absolute;
  top: 655px;
}

.recentlymovie {
  position: absolute;
  top: 1185px;
}

.reco {
  position: absolute;
  top: 1715px;
  margin-left: 60px;
  margin-top: 3px;
}
</style>
