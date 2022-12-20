from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

week_days_dict={
    'monday': 'Сегодня понедельник',
    'tuesday': 'Сегодня вторник',
    'wednesday': 'Сегодня среда',
    'thursday': 'Сегодня четверг',
    'friday': 'Сегодня пятница',
    'saturday': 'Сегодня суббота',
    'sunday': 'Сегодня воскресенье',
}

def get_info_about_weekday(request, day_week):
    description = week_days_dict.get(day_week)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Неизвестный день недели - {day_week}')

def get_info_about_weekday_by_number(request, day_week):
    week_days = list(week_days_dict)
    name_week_day = week_days[day_week-1]
    if day_week > 0 and day_week < 8:
        redirect_url = reverse('weekday-name', args=(name_week_day, ))
        return HttpResponseRedirect(redirect_url)
    else:
        HttpResponseNotFound(f'Неправильный порядковый номер дня недели - {day_week}')
