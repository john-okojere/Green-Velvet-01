from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('api/menus/', views.get_menus, name='get-menus'),
    path('africanMenu/', views.africanMenu, name='africanMenu'),
    path('internationalMenu/', views.internationalMenu, name='internationalMenu'),
    path('drinkMenu/', views.drinkMenu, name='drinkMenu'),
]
