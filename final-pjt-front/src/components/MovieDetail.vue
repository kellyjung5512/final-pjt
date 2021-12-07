<template>
  <div class="d-flex">
    <div>
    <button
     v-if="isLikeStatus" 
     @click="like" 
     class="btn btn-like" 
     style="padding: 16px 32px; margin: 4px 6px; font-size: 16px; display: inline-block; cursor: pointer; transition-duration: 0.4s;"
    ><i class="fas fa-heart"></i> {{ likeCount }}</button>
    <button 
      v-else
     @click="like" 
     class="btn btn-dislike" 
     style="padding: 16px 32px; margin: 4px 6px; font-size: 16px; display: inline-block; cursor: pointer; transition-duration: 0.4s;"
    ><i class="far fa-heart"></i> {{ likeCount }}</button>
    </div>
    <div>
    <button 
      @click="handleClickButton" 
      class="btn btn-detail" 
      style="padding: 16px 32px; margin: 4px 6px; font-size: 16px; display: inline-block; cursor: pointer; transition-duration: 0.4s;"
    >상세 정보</button>
    </div>

    <app-modal :visible.sync="visible">
      <h2 style="font-weight: bold;">{{ movie.title }}</h2>
      <hr>
      <!-- <div class="video-container">
        <iframe :src="videoURI" frameborder="0" allow="fullscreen"></iframe>
      </div> -->
      <div class="mt-4 d-flex align-items-center">
        <br>     
        <div class="col">
          <p v-if="movie.genres[0] === 28">장르 : 액션 </p>
          <p v-if="movie.genres[0] === 16">장르 : 애니메이션 </p>
          <p v-if="movie.genres[0] === 35">장르 : 코미디 </p>
          <p v-if="movie.genres[0] === 80">장르 : 범죄 </p>
          <p v-if="movie.genres[0] === 99">장르 : 다큐멘터리 </p>
          <p v-if="movie.genres[0] === 12">장르 : 어드벤쳐 </p>
          <p v-if="movie.genres[0] === 18">장르 : 드라마 </p>
          <p v-if="movie.genres[0] === 10751">장르 : 가족 </p>
          <p v-if="movie.genres[0] === 14">장르 : 판타지 </p>
          <p v-if="movie.genres[0] === 36">장르 : 역사 </p>
          <p v-if="movie.genres[0] === 27">장르 : 호러 </p>
          <p v-if="movie.genres[0] === 10402">장르 : 음악 </p>
          <p v-if="movie.genres[0] === 9648">장르 : 미스터리 </p>
          <p v-if="movie.genres[0] === 10749">장르 : 로맨스 </p>
          <p v-if="movie.genres[0] === 878">장르 : 공상과학 </p>
          <p v-if="movie.genres[0] === 10770">장르 : TV Movie </p>
          <p v-if="movie.genres[0] === 53">장르 : 스릴러 </p>
          <p v-if="movie.genres[0] === 10752">장르 : 전쟁 </p>
          <p v-if="movie.genres[0] === 37">장르 : 서부 영화 </p>
          <p v-if="!movie.genres[0]">업데이트 예정입니다.</p>        
          <p>평점 : {{ movie.vote_average }}점</p>
          <p>상영 시간 : {{ movie.runtime }}분</p>
          <p>개봉 일자 : {{ movie.release_date }}</p>
          <p v-if="movie.overview">{{ movie.overview }}</p>
          <p v-if="!movie.overview">업데이트 예정입니다.</p>
        </div>
      </div>
      <hr>
    </app-modal>
  </div>
</template>

<script>
import Modal from './Modal'
import _ from 'lodash'
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL
// const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
// const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'MovieDetail',
  data: function () {
    return {
      visible: false,
      person: [],
      islike: '',
      likeCount: '',
      // videoURI: '',
      // videoId: '',
      rating: Number(this.movie.vote_average),
    }
  },
  props: {
    movie: Object,
  },
  components: {
    appModal: Modal,
  },
  methods: {
    handleClickButton: function () {
      this.visible = !this.visible
      this.fetchVideo()
    },
    ratingToInt: function () {
      this.rating = Math.ceil(this.rating / 2)
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
        this.person = res.data
        if (this.person.like_movies.includes(this.movie.id)) {
          this.islike = true
        } else {
          this.islike = false
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },
    like: function () {
      const config = this.getToken()
      const item = {
        myId: this.person.id,
        movieId: this.movie.id,
      }
      axios.post(`${SERVER_URL}/movies/${this.person.id}/${this.movie.title}/like/`,item ,config)
      .then(() => {
        this.getMyProfile()
        this.likecheck()
      })
      .catch((err) => {
        console.log(err)
        alert('오류가 발생하였습니다.')
      })
    },
    likenumber: function () {
      this.likeCount = this.movie.like_users.length
    },
    likecheck: function () {
      if (this.islike) {
        this.likeCount--
      } else {
        this.likeCount++
      }
    },
    // fetchVideo() {
    //  const params = {
    //     key: API_KEY,
    //     part: 'snippet',
    //     type: 'video',
    //     q: this.movie.title + 'trailer'
    //   }
    //   axios.get(API_URL, { params, })
    //   .then((res) => {
    //     this.videoId = res.data.items[0].id.videoId        
    //     this.videoURI = `https://www.youtube.com/embed/${this.videoId}?autoplay=1&mute=1`
    //   })
    // },
  },
  computed: {
    isLikeStatus: function () {
      return this.islike
    },
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  },
  created: function () {
    this.getMyProfile()
    this.likenumber()
    this.ratingToInt()
  }

}
</script>


<style scoped>
.video-container > iframe {
  width: 600px;
  height: 400px;
}
.btn {
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 6px;
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
  cursor: pointer;
  
}
.btn-like {
  background: linear-gradient(-45deg, #b98da6 0%, #fd11d685 100%);
  color: white;
}
.btn-dislike {
  background: rgba(128, 116, 141, 0.2);
  color: white;
}
.btn-detail{
  background: linear-gradient(125deg,#586d6d,#4d40b6,#b13e51);
  color: white;
  width: 112%;
}
.col p {
  margin-bottom: 12px;  
}
          
</style>