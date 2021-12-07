<template>
<div class="col">
  <div class="card" style="width: 18rem; background-color: rgba(0, 0, 0, 0);">      
    <img :src="movieImage" alt="poster_path" class="m-2" style="object-fit: fill; height: 24rem;">       
    <MovieDetail :movie="movie"/>        
  </div>
</div>
</template>

<script>
import MovieDetail from '@/components/MovieDetail'


export default {
    name:'MovieCard',
    components: {
        MovieDetail,
    },
    props: {
      movie: Object,
    },
    computed:{
      movieImage: function () {
        return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}` 
       },
    },

}
</script>

<style scoped>
.card:hover img{
  transform: scale(1.05);
  box-shadow: 0 10px 20px rgba(197, 182, 188, 0.623), 0 4px 8px rgba(0,0,0,.06);
}
</style>