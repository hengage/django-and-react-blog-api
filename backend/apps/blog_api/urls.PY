from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'blog_api'


urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail_create'),
    path('', views.PostList.as_view(), name='post_list_create'),
]