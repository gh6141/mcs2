from django.shortcuts import render

from django.http import HttpResponse


def top(request):
    return HttpResponse(b"Test Test")



# Create your views here.

def mcsmain_new(request):
    return HttpResponse('登録')


def mcsmain_edit(request, mcsmain_id):
    return HttpResponse('編集')


def mcsmain_detail(request, mcsmain_id):
    return HttpResponse('詳細閲覧')

