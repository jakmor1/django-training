from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index_view, name="index"),
    path('<source>/', views.index_view, name="index"),
]