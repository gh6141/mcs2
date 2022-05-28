from django.http import HttpResponse
from django.views.generic import TemplateView

def testfunc(request):
    return HttpResponse('test')

def top(request):
    return HttpResponse('test')

class Hclass(TemplateView):
    template_name='test2.html'

