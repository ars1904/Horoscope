from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area, name='calc-rectangle-name'),
    path('square/<int:width>', views.get_square_area, name='calc-square-name'),
    path('circle/<int:radius>', views.get_circle_area, name='calc-circle-name'),
    path('get_rectangle_area/<int:width>/<int:height>', views.get_rectangle_area_new),
    path('get_square_area/<int:width>', views.get_square_area_new),
    path('get_circle_area/<int:radius>', views.get_circle_area_new),
]