from django.shortcuts import render
from django.views.generic import TemplateView

def Func_template(request):
    return render(request, 'func_template.html')

class Class_template(TemplateView):
    template_name = 'class_template.html'