from . import views

from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('bookmarks/', views.index, name='index'),
    path('bookmarks/<int:folder_id>/', views.contents, name='contents'),
]
