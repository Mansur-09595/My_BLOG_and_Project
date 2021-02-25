from django.urls import path

from. import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
     path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('about/', views.About.as_view(), name='about'),
]