from django.urls import include, path
from elsys import views

urlpatterns = [
    path('', views.index),
    path('min_temp', views.min_temp),
    path('max_temp', views.max_temp),
    path('avg_temp', views.avg_temp)
]
