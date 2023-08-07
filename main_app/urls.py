from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('foxes/', views.foxes_index, name='index'),
    path('foxes/<int:fox_id>/', views.foxes_detail, name='detail'),
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
 ]