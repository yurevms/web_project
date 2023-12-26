from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('rules/', views.rules, name='rules'),
    path('info/', views.info, name='info'),
    path('<int:id>/', views.details, name='details'),
    path('review/<int:id>/', views.comm, name='comments'),
]
