from django.shortcuts import render, redirect
from .models import *


def index(request):
    context = {
        'dojos': Dojo.objects.all(),
        'ninjas': Ninja.objects.all()
    }
    return render(request, 'index.html', context)


def dojos(request):
    print(request.POST)
    Dojo.objects.create(
        name=request.POST["name_of_dojo"],
        city=request.POST["city"],
        state=request.POST["state"]
    )
    return redirect('/')


def ninjas(request):
    print(request.POST)

    dojo_from_db = Dojo.objects.get(id=request.POST["dojo"])

    Ninja.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        dojo_id=dojo_from_db
    )
    return redirect('/')
