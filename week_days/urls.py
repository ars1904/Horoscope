from django.urls import path
from . import views

urlpatterns = [
    path('<int:day_week>/', views.get_info_about_weekday_by_number),
    path('<str:day_week>/', views.get_info_about_weekday, name='weekday-name'),
]