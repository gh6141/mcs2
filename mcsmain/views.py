from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


from mcsmain.models import Mcsmain


def top(request):
    mcsmain = Mcsmain.objects.all()
    context = {"mcsmain": mcsmain}
    return render(request, "mcsmain/top.html",context)



# Create your views here.

def mcsmain_new(request):
    return HttpResponse('登録')


def mcsmain_edit(request, mcsmain_id):
    return HttpResponse('編集')


def mcsmain_detail(request, mcsmain_id):
    mcsmain = get_object_or_404(Mcsmain, pk=mcsmain_id)
    return render(request, 'mcsmain/mcsmain_detail.html',
                  {'mcsmain': mcsmain})

