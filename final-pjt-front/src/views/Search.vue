<template>
  <div class="pb-5">
    <div class="searchbar">
      <b-form @submit.prevent="onSearch">
        <input
        type="text" 
        class="mt-3 col-md" 
        style="width: 100%; height: 3rem; color: white; "
        v-model="keyword"        
        placeholder="영화 제목을 입력하시오.">
      </b-form>
    </div>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <div>
      <MovieText v-if="movieList" class="d-flex justify-content-center" :text="'검색 결과'" style="font-size: 3rem;"/>
      <MovieList :movieList="movieList"/>
    </div>
  </div>
</template>

<script>
import MovieList from "../components/MovieList"
import MovieText from "../components/MovieText"
import { movieApi } from '../utils/axios'
import { mapMutations } from "vuex"
export default {
  name: "Search",
  data: function() {
    return {
        keyword:"",
        movieList:""
      }
    },
  components:{
      MovieText,
      MovieList
  },
created(){
  this.SET_LOADING(false);
},
methods:{
  ...mapMutations(["SET_LOADING"]),
  async onSearch(){
      this.SET_LOADING(true);
      console.log(this.keyword);
      if(!this.keyword){
          alert("영화 제목을 입력하세요.");
          this.keyword = ""
          return;
      }
      const {data} = await movieApi.search(this.keyword);
      console.log(data);
      this.movieList=data.results;
      this.SET_LOADING(false);
      this.keyword = ""
  }    
}

}
</script>

<style scoped>
::placeholder {
  color: white;
  font-size: 20px;
  font-weight: 100%;
  display: flex;
  text-align: center;
  opacity: 1; /* Firefox */
}
.searchbar {
  border-bottom: 1px solid #fff; 
  overflow: hidden; 
  position: absolute;
  left: 37.5%; 
  top: 100px; 
  width: 25%; 
  height: 60px;
}
</style>