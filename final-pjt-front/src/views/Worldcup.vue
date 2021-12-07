<template>
  <div class="ibox-content">
    <div class="wleft" :style="first_movie | imageURL | backgroundStyle" @click="selectMovie(first_movie)" ref="wleft"></div>
    <div class="wright" :style="second_movie | imageURL | backgroundStyle" @click="selectMovie(second_movie)" ref="wright"></div>
    <div class="versus" ref="versus"></div>
    <div class="title">당신의 최고의 영화는?<br>      
      <span v-if="max_count > 2">16강 {{ count }}/{{ max_count }}</span>
      <span v-else-if="max_count> 1 ">4강 {{ count }}/{{ max_count }}</span>
      <span v-else>결승전</span>      
    </div>
  </div>
</template>

<script>
import best2 from "@/best/best2"
import { mapState } from 'vuex'
import { mapActions } from 'vuex'
import axios from 'axios'
import _ from 'lodash'

const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: "Worldcup", 
  data: function() {
    return {
      movies: [],
      first_movie: Object,
      second_movie: Object,
      count: 1,
      max_count: 8,
      checkDouble: true,
    }
  },
  methods : {
    ...mapActions([
      'setNextPage'
    ]),
    setToken: function () {
      const token = localStorage.setItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    getMovies: function() {
      const headers = this.setToken()
      
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/worldcup`,
        headers,
      })
      .then((res) => {
        this.movies = res.data
        this.first_movie = this.movies.shift()
        this.second_movie = this.movies.shift()
        this.movies = _.shuffle(this.movies)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    selectMovie: function(select_movie) {      
      if (this.checkDouble) {
        this.checkDouble = false
        this.count++
        if (this.count > this.max_count) {
          this.count = 1
          this.max_count = this.max_count / 2
        }
        this.movies.push(select_movie)        
      }
    },
  },
  best: [best2],
  computed: {
    ...mapState([
      'token'
    ])
  },
  filters: {
    backgroundStyle: function (url) {
      return `background-image: url('${url}')`
    }
  },
  created : function() {
    if (!this.token){
      const res = {
        name: 'Worldcup',
      }
      this.setNextPage(res)
      // this.$router.push({name : 'Login'})
    } 
    // this.getMovies()
  }
}
</script>
<style>
.ibox-content {
  height:90vh;
  text-align:center;
  padding:0px;
}
.ibox-content .wleft{
  width:50%;
  height:100%;
  max-width:50%;
  max-height:100%;  
  background-repeat:no-repeat;
  background-size:contain;
  background-position:right center;
  position:relative;
  z-index:1;  
}
.ibox-content .wright{
  width:50%;
  height:100%;
  max-width:50%;
  max-height:100%;  
  background-repeat:no-repeat;
  background-size:contain;
  background-position:left center;
  position:relative;
  left:50%;top:-100%;
  z-index:2;
}
.ibox-content .versus{
  width:100%;
  height:calc(7 * (1vw + 1vh - 1vmin));
  max-width:100%;
  max-height:50%;
  background-image:url('../assets/images/vs.jpg');
  background-repeat:no-repeat;
  background-size:contain;
  background-position:center top;
  position:relative;
  left:0%;
  top:-155%;
  z-index:3;
  pointer-events:none;
}
.ibox-content .title{
  width:100%;
  height:calc(3 * (1vw + 1vh - 1vmin));
  max-width:100%;
  max-height:50%;
  position:relative;
  left:0%;
  top:-200%;
  transform: translateY(-100%);
  z-index:4;
  line-height:calc(3 * (1vw + 1vh - 1vmin));
  background-color: rgba( 0, 0, 0, 0.5 );
  color:white;
  font-size:calc(2.5 * (1vw + 1vh - 1vmin))  
} 
.ibox-content .text {
  width:100%;
  height:calc(7 * (1vw + 1vh - 1vmin));
  max-width:100%;
  max-height:50%;
  position:relative;
  left:0%;
  top:-155%;
  z-index:4;
  color:white;
  font-size:calc(2 * (1vw + 1vh - 1vmin));
  text-shadow:-1px 0 #000000,0 1px #000000,1px 0 #000000,0 -1px #000000;
  -moz-text-shadow:-1px 0 #000000,0 1px #000000,1px 0 #000000,0 -1px #000000;
  -webkit-text-shadow:-1px 0 #000000,0 1px #000000,1px 0 #000000,0 -1px #000000;
  pointer-events:none;
}
.ibox-content .text #wleftn{
  width:50%;
  display:inline-block;
  text-align:right;
  padding-right:10%
}
.ibox-content .text #wrightn{
  width:50%;
  display:inline-block;
  text-align:left;
  padding-left:10%
}
</style>