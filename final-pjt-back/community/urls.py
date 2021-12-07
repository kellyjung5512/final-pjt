from django.urls import path
from . import views


urlpatterns = [
    path('', views.community_list_create, name='index'),                                                # 게시글 작성 및 생성
    path('<int:community_pk>/', views.community_detail, name='detail'),                                 # 개별 게시글 조회    
    path('<int:community_pk>/comments/', views.comments, name='comments'),                              # 코멘트 작성
    path('<int:community_pk>/comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'), # 코멘트 조회
]