from django.shortcuts import get_object_or_404
from .models import Movie
from django.contrib.auth import get_user_model
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random

@api_view(['GET'])
def movies(request):
    movies = Movie.objects.all()
    popular_movies = Movie.objects.all().order_by('-vote_average')[:120] # 평점
    latest_movies = Movie.objects.all().order_by('-release_date')[:30]  # 최신영화
    interest_movies = Movie.objects.all().order_by('-popularity')[:120]  # 인기
    # cinema_version_movies = Movie.objects.filter(title__contains="극장판").values()

    serializer = MovieSerializer(movies, many=True)
    popular_serialize = MovieSerializer(popular_movies, many=True)
    latest_serializer = MovieSerializer(latest_movies, many=True)
    interest_serializer = MovieSerializer(interest_movies, many=True)
    # cinema_version_movies_serializer = MovieSerializer(cinema_version_movies, many=True)

    return Response([serializer.data, popular_serialize.data, latest_serializer.data, interest_serializer.data])


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def movie_like(request, my_pk, movie_title):
  movie = get_object_or_404(Movie, title=movie_title)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_movies.filter(pk=movie.pk).exists():
      me.like_movies.remove(movie.pk)
      islike = False      
  else:
      me.like_movies.add(movie.pk)
      islike = True
  
  return Response(islike)


# 영화 월드컵 구현 실패
# @api_view(['GET', 'POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def worldcup(request) :
#     if request.method == 'GET' :
#         random_movies = random.sample(list(Movie.objects.all()), 16)
#         serializer = MovieSerializer(data=random_movies, many=True)
#         return Response(serializer.data)
#     elif request.method =='POST' : 
#         movie_id = request.data["movie_id"]
#         movie = Movie.objects.get(pk=movie_id)
#         worldcup = Worldcup.objects.create(movie=movie, user=request.user)
#         serializer = WorldcupSerializer(data=worldcup)
#         return Response(serializer.data)

