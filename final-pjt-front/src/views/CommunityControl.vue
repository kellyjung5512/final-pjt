<template>
  <div class="container create-community-form" style="position: relative; top: 150px;">
    <!-- <h2 class="text-center">Create a post</h2> -->
    <div class="">
      <h2 class="text-center">게시글 수정</h2>
      <div class="row">
        <div class="form-group my-3">
          <label for='title'>제목</label>
          <input class="form-control" id="title" type="text" v-model.trim="community.title" required='required' placeholder="제목을 입력하시오">
        </div>
        <div class="clearfix"></div>
        <div class="form-group my-3">
          <label for="content">내용</label>
          <textarea class="form-control" id="content" rows="5" v-model.trim="community.content" required='required' placeholder="내용을 입력하시오"></textarea>
        </div>
      </div>
      <div class="col-md-12 form-group my-3">
        <button class="btn btn-success" @click="updateCommunity(community)">저장</button>
      </div>
    </div>
  </div>    

</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CommunityControl',
  props: {
    community_pk: Number,
  },
  data: function () {
    return {
      community: [],
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
      const community_pk = this.$route.params.community_pk
      axios.get(`${SERVER_URL}/community/${community_pk}/`, config)
        .then((res) => {
          this.community = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateCommunity: function (community) {
      const config = this.getToken()
      const community_pk = this.$route.params.community_pk
      const communityItem = {
        title: community.title,
        content: community.content,
      }
      axios.put(`${SERVER_URL}/community/${community_pk}/`, communityItem, config)
      .then((res) => {
        if (res.data.message) {
          alert("작성자만 수정할 수 있습니다.")
        }
        else {
          this.$router.push({ name: 'CommunityDetail', params: { community_pk: `${community_pk}` }})
        }
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created: function () {
    this.getCommunity()
  }
}
</script>

<style>

</style>