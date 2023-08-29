from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('start/', views.home_view, name="start"),
    path('contact/', views.contact_view, name="contact"),
    path('about/', views.about_view, name="about"),
    path('about-me/', views.about_view),
    path('genbank/', views.genbank_view),
]