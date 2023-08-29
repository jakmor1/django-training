from django.urls import path

from . import views

app_name = 'covid19'

urlpatterns = [
    path('', views.index_view, name="index"),
    path('<country_code>/', views.index_view, name="index"),
]
