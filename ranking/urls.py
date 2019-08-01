from django.urls import path
from .views import barRankListView,upload ,loginfunc,logout_view

app_name = 'barRankCsv'
urlpatterns = [
    path('list/', barRankListView.as_view(),name='list'),
    path('login/',loginfunc,name='login'),
    path('logout/',logout_view,name='logout'),
]
