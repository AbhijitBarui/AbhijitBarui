from django.shortcuts import redirect, render
from .models import Routine
from datetime import datetime
from .forms import RoutineForm
weekday = datetime.today().strftime('%A')


def routine(request):
    # routine = Routine.objects.all().filter(day=datetime.today().strftime('%A'))
    routines = Routine.objects.all().filter(day=weekday)
    context = {
        'routines':routines,
    }
    return render(request, 'routines/routine.html', context)


def getroutine(request):
    form = RoutineForm
    context = {
        'form':form,
    }
    return render(request, 'routines/routineform.html', context)

def postroutine(request):
    form = RoutineForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('routine')