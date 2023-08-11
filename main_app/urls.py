from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('foxes/', views.foxes_index, name='index'),
    path('foxes/<int:fox_id>/', views.foxes_detail, name='detail'),
    path('foxes/create/', views.FoxCreate.as_view(), name='foxes_create'),
    path('foxes/<int:pk>/update/', views.FoxUpdate.as_view(), name='foxes_update'),
    path('foxes/<int:pk>/delete/', views.FoxDelete.as_view(), name='foxes_delete'),
    path('foxes/<int:fox_id>/add_habitats/', views.add_habitats, name='add_habitats'),
    path('foxes/<int:fox_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('foxes/<int:fox_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('accounts/signup/', views.signup, name='signup'),
 ]