<template>
  <div class="container community-form">
    <div>
      <div class="text-start title">
        <h3>{{ community.title }}</h3>
      </div>
      <div class="text-end info" style="margin-top:13px">
        <h6>글쓴이: {{ community.auth_user }} 작성일자: {{ community.created_at|yyyyMMdd }}</h6>
      </div>
      <hr style="color:white; border:solid 2px">
    </div>
    <!-- <hr style="color:white"> -->
    <div class="content-box">
      <h5 class="content text-start">{{ community.content }}</h5>
    </div>
    <div class="d-flex justify-content-center" style="margin: 15px">
      <button 
      class="btn btn-update" 
      v-if="community.auth_user === currentUser" 
      @click="updateCommunity"
      >수정</button>
      <button
      class="btn btn-delete"
      @click="deleteCommunity"
      v-if="community.auth_user === currentUser"
      >삭제</button>
    </div>

    <section>
      <div class="container comment-box">
        <img :src="CommentList" alt="" class="d-flex justify-content-flex-start" style="margin-top:7px;">
        <hr style="color:white;">
        <div class="container" style="color:white; padding-bottom: 10px" v-for="(comment, idx) in comments" :key="idx">
          <span class="d-flex justify-content-start" style="margin-left: 70px">{{ comment.auth_user }}님 : {{ comment.content }}<i class="fas fa-times" style="color:red; margin-left:10px; margin-top: 5px;" @click="deleteComment(community, comment)"
          v-if="comment.auth_user === currentUser"></i></span>
        </div>
        <!-- <h2>댓글 작성</h2> -->
        <div class="d-flex justify-content-center" style="padding-bottom: 15px;">
          <input class="comment-input" @keypress.enter="createComments" v-model.trim="comment_content" type="text" id="comment" placeholder="댓글을 달아주세요." required="required">
          <button class="comment-botton" @click="createComments">작성</button>
        </div>
      </div>
    </section>
  </div>  
</template>

<script>
import axios from 'axios'
import VueJwtDecode from "vue-jwt-decode"
import jwt_decode from "jwt-decode"
import CommentList from "@/assets/images/commentlist.png"

const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'CommunityDetail',
  props: {
    community_pk: Number,
  },
  data: function () {
    return {
      community: [],
      user: [],
      comments: [],
      comment_content: '',
      currentUser:'',
      CommentList,
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
    getCommunity: function () {
      const config = this.getToken()
      const token = localStorage.getItem('jwt')
      const decoded = jwt_decode(token)
      this.currentUser = decoded.username
      // console.log(this.currentUser)
      const community_pk = this.$route.params.community_pk
      axios.get(`${SERVER_URL}/community/${community_pk}`, config)
        .then((res) => {
          this.community = res.data
          // console.log(this.community.userName)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getUser: function () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)

      axios.get(`${SERVER_URL}/accounts/profile/`, info, config)
      .then((res) => {
        this.user = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    deleteCommunity: function () {
      const config = this.getToken()
      const community_pk = this.$route.params.community_pk
      axios.delete(`${SERVER_URL}/community/${community_pk}`, config)
      .then(() => {
          this.$router.push({ name: 'Community' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    updateCommunity: function (community) {
      const community_pk = this.$route.params.community_pk
      console.log(this.user)
      if (this.user.username == community.userName) {
        this.$router.push({ name: 'CommunityControl', params: {community_pk: `${community_pk}`}})
      } else {
        alert("작성자만 변경할 수 있습니다.")
      }
    },
    // 댓글 시작
    getComments: function () {
      const config = this.getToken()
      const community_pk = this.$route.params.community_pk
      axios.get(`${SERVER_URL}/community/${community_pk}/comments/`, config)
        .then((res) => {
          this.comments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    createComments: function () {
      const config = this.getToken()
      const community_pk = this.$route.params.community_pk
      // const comment_pk = this.$route.params.comment_id
      const commentItem = {
        content: this.comment_content
      }
      if (commentItem.content) {
        axios.post(`${SERVER_URL}/community/${community_pk}/comments/`, commentItem, config)
          .then(() => {
            this.getComments()
            this.comment_content = ''
          })
      }
    },
    deleteComment: function (community, comment) {
      const config = this.getToken()
      const token = localStorage.getItem('jwt')
      const decoded = jwt_decode(token)
      this.currentUser = decoded.username
      // const community_pk = this.$route.params.community_pk
      axios.delete(`${SERVER_URL}/community/${community.id}/comments/${comment.id}`, config)
        .then((res) => {
          if (res.data.status == "FAIL") {
            alert("작성자만 삭제할 수 있습니다.")
          } else {
            this.getComments()
          }
        })
      },
    },
  computed: {
    commentsList: function () {
      return this.comments
    }
  },
  created: function () {
    this.getCommunity()
    this.getComments()
  },
    filters : {  
    yyyyMMdd : function(value){ 
      if(value == '') return '';
      let js_date = new Date(value);
      let year = js_date.getFullYear();
      let month = js_date.getMonth() + 1;
      let day = js_date.getDate();
      if(month < 10){
        month = '0' + month;
      }
      if(day < 10){
        day = '0' + day;
      }
      return year + '-' + month + '-' + day;
    }
  }
}
</script>

<style>
.community-form {
  box-sizing: border-box;
  margin: 20px auto 10px;
  background-color: rgb(255, 255, 255, 0);
  color: black;
  border: solid rgb(255, 255, 255, 0) 1px;
  border-radius: 4px;
  position: relative;
  top: 150px;

}
.title h3 {
  font-weight: bold;
  padding-top: 20px;
  margin-left: 20px;
  letter-spacing: .05em;
  color: white;
  text-align: left;
}

.content {
  margin-left: 20px;
  padding-top: 10px;
  padding-bottom: 15px;
  color: white;
}

.info {
  color: gray;
  line-height: 1;
  letter-spacing: .05em;
}

.btn-delete {
  background: linear-gradient(125deg,#c7705b,#992793,#ebbfc7) !important;
  color: white !important;
}

.btn-update {
  background: linear-gradient(125deg,#1e472f,#175009,#358566) !important;
  color: white !important;
}

.content-box {
  padding: 5px;
  height: 200px;
}

.comment-box {
  border: white 2px solid;
  height: auto;
  padding: 10px;
}

.comment-input {
  border: white 1px solid;
  background-color: rgb(0, 0, 0, 0.01);
  border-radius: 4px;
  margin-top: 10px;
  width: 80%;
  height: 50px;
  /* display:flexbox; */
  color: white;
  padding-left: 10px;
  margin-right: 1%;
}

.comment-botton {
  border: none;
  border-radius: 4px;
  margin-top: 10px;
  background: linear-gradient(125deg,#4a525281,#565669,#202020);
  color:white;
  width: 7%;
  height: 50px;
}

::placeholder {
  color: white;
  font-size: 15px;
  font-weight: 100%;
  display: flex;
  text-align: start;
  opacity: 1;
  padding-left: 10px;
}
</style>