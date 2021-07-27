from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    year = request.GET.get("year", "")
    return HttpResponse(f'Hello, world! {year}')
