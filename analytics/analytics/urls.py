from django.urls import path
from . import views
urlpatterns = [
    path('', views.base, name='home'),
    path('dashboard/<str:city>/', views.dashboard,name='dashboard'),
    path('dashboard/bangalore/', views.dashboard,name='banglore'),
    path('dashboard/delhi/', views.dashboard,name='delhi'),
    path('dashboard/chennai/', views.dashboard,name='chennai'),
    path('api/aqi-data/<str:city>', views.PollutionDataAPIView.as_view(),name='api-data'),
    path('api/aqi-data/bangalore', views.PollutionDataAPIView.as_view(),name='bangapi'),
    path('api/aqi-data/delhi', views.PollutionDataAPIView.as_view(),name='delapi'),
    path('map/',views.map,name='map'),
]
