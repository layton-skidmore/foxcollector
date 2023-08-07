from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('foxes/', views.foxes_index, name='index'),
    path('foxes/<int:fox_id>/', views.foxes_detail, name='detail'),
    path('foxes/create/', views.FoxCreate.as_view(), name='foxes_create'),
    path('foxes/<int:pk>/update/', views.FoxUpdate.as_view(), name='foxes_update'),
    path('foxes/<int:pk>/delete/', views.FoxDelete.as_view(), name='foxes_delete')
 ]