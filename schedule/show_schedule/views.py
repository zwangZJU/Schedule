from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Why are you here?")

from .models import Week
def week(request):
    week_list = Week.objects.all()
    return render(request,'show_schedule/weeks.html',{"weeks":week_list})

from .models import  Plan
def plan_detail(request):
    plan_list = Plan.objects.all()
    return render(request,'show_schedule/plans.html',{"plans":plan_list})

def find_plan_by_week(request,week_number):
    week = Week.objects.get(number=week_number)
    plan_list = week.plan_set.all()
    return render(request, 'show_schedule/plans.html', {"plans": plan_list,"week":week})
