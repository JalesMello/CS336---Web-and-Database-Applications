from django.shortcuts import render
from registration.models import Workshop


# Create your views here.
def workshopschedule(request):
    workshop1a = Workshop.objects.get(id="1")
    workshop1b = Workshop.objects.get(id="2")
    workshop1c = Workshop.objects.get(id="3")
    workshop2a = Workshop.objects.get(id="4")
    workshop2b = Workshop.objects.get(id="5")
    workshop2c = Workshop.objects.get(id="6")
    workshop3a = Workshop.objects.get(id="7")
    workshop3b = Workshop.objects.get(id="8")
    workshop3c = Workshop.objects.get(id="9")
    return render(request, 'workshopschedule.html', {'1A': workshop1a, '1B': workshop1b, '1C': workshop1c,
                                                     '2A': workshop2a, '2B': workshop2b, '2C': workshop2c,
                                                     '3A': workshop3a, '3B': workshop3b, '3C': workshop3c})
