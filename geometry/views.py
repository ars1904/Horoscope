from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from math import pi
from django.urls import reverse
# Create your views here.

def get_rectangle_area(request,width,height):
    if width > 0 and height > 0:
        return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')
    else:
        return HttpResponseNotFound(f'Введите положительные значения')

def get_square_area(request, width):
    if width > 0:
        return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width * width}')
    else:
        return HttpResponseNotFound(f'Введите положительное значение')

def get_circle_area(request, radius):
    if radius > 0:
        return HttpResponse(f'Площадь круга с радиусом {radius} равна {round(pi*(radius**2))}')
    else:
        return HttpResponseNotFound(f'Введите положительное значение')
def get_rectangle_area_new(request,width,height):
    redirect_url = reverse('calc-rectangle-name', args=(width, height, ))
    return HttpResponseRedirect(redirect_url)

def get_square_area_new(request, width):
    redirect_url = reverse('calc-square-name', args=(width, ))
    return HttpResponseRedirect(redirect_url)

def get_circle_area_new(request, radius):
    redirect_url = reverse('calc-circle-name', args=(radius, ))
    return HttpResponseRedirect(redirect_url)