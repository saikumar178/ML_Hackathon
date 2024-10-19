from django.urls import path
from .views import home, register_volunteer, geolocation, report_disaster, disaster_list
from . import views
from .views import register_volunteer, thanks_view

urlpatterns = [
    path('', home, name='home'),  # This is your index page
    path('register/', register_volunteer, name='register_volunteer'),
    path('geolocation/', geolocation, name='geolocation'),
    path('report/', report_disaster, name='report_disaster'),
    path('disasters/', disaster_list, name='disaster_list'),
    path('register/', register_volunteer, name='register_volunteer'),
     path('register/', views.register_volunteer, name='register_volunteer'),
     path('thanks/', thanks_view, name='thanks'),  # Add this line
     path('thanks/', views.thanks_view, name='thanks'),
      path('', views.index_view, name='index'),
]
