from . import views

from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:folder_id>/', views.contents, name='contents'),
]
