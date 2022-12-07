from django.urls import path

from blog import views

# from blog.models import Blog

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('blog/new/', views.HomeCreateView.as_view(), name='create'),
    path('blog/<int:pk>/', views.HomeDetailsView.as_view(), name='details'),
    path('blog/<int:pk>/edit/', views.HomeUpdateView.as_view(), name='update'),
    path('blog/<int:pk>/delete/', views.HomeDeleteView.as_view(), name='delete'),
]
