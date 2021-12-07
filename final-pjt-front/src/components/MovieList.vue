<template>
  <div class="d-flex flex-wrap justify-content-center" v-if="movieList">
    <div
      class="card"
      style="width: 20rem; background-color: rgba(0, 0, 0, 0);"
      v-for="movie in movieList"
      :key="movie.id"
    >
      <div @click="goDetail(movie.id)" v-if="movie">
        <b-img style="object-fit: fill; height: 24rem; margin-left: 20px;" v-if="movie.poster_path" fluid :src="image(movie.poster_path)" alt="Image 2"></b-img>
        <b-img style="object-fit: fill; height: 24rem; margin-left: 20px;" v-else fluid :src="noImage" alt="Image 2"></b-img>
        <span class="movie-title2 text-center fs-4">{{ movie.title }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieList',
  props: ['movieList'],
  data() {
    return {
      noImage: require("@/assets/noimage.png")
    }
  }
,
  methods: {
    image(img) {
      return `https://image.tmdb.org/t/p/w300/${img}`;
    },
    goDetail(id){
      this.$router.push(`/${id}`);
    }
  },
};
</script>

<style>
.movie-title2 {
  margin-top: 5px;
  margin-bottom: 25px;
  display: flex;
  justify-content: center;
}
</style>