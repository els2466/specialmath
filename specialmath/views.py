from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .functions import specialMath

# def index(req, num=0):
#     return HttpResponse('ok, we are live - the num = %s' % specialMath(num))

def index(request, num=0):
    context = {
        'title':'WISP',
        'function':'SpecialMath function',
        'input_number': num,
        'output_number': specialMath(num)
    }
    return render(request, 'home_page.html', context)
