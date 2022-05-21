from django.shortcuts import render

def routine(request):
    return render(request, 'routines/routine.html')