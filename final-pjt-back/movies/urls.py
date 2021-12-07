from django.urls import path
from . import views

urlpatterns = [    
    path('', views.movies),                                      # 전체 영화 목록 (랜덤 30개 + 평점 순으로 나열된 목록 + 최신 영화 개봉 순으로 나열된 목록)
    path('<int:movie_pk>/', views.movie_detail),                 # 영화 상세페이지 -> Vue-modal   
    path('<int:my_pk>/<movie_title>/like/', views.movie_like),   # 좋아요 클릭                                                               
    # path('worldcup', views.worldcup),                          # 영화 월드컵 (구현 실패)
]