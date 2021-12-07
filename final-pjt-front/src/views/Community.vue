<template>
  <div class="container" style="position:relative;">
      <h2><span class="span-h2">자유게시판</span></h2>
      <CommunityList :communities="communities"/>
      <!-- <CreateCommunity @community-created="communityCreated"/> -->      
  </div>
</template>

<script>
import CommunityList from '@/components/CommunityList'
// import CreateCommunity from '@/components/CreateCommunity'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'Community',
  components: {
    CommunityList,
    // CreateCommunity,
  },
  data: function () {
    return {
      communities: [],
      user: [],
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
    getCommunities: function () {
      const config = this.getToken()

      axios.get(`${SERVER_URL}/community/`, config)
      .then((res) => {
        // console.log(res)
        this.communities = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    communityCreated: function () {
      this.getCommunities()
    },
  },
  created: function () {
    this.getCommunities()
  },
}
</script>

<style scoped>
.span-h2 {
  /* text-transform: uppercase; */
  font-size: 25px; 
  font-weight: bold; 
  letter-spacing: .1em; 
  position: absolute;
  top: 150px;
  left: 45.25%;
}

</style>