from django.shortcuts import render
from registration.forms import RegistrationForm


def registration(request):
    if request.method == 'post':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save(commit=True)
            new_registration = registration_form.cleaned_data
            return render(request, 'thankyou.html', {'new_registration': new_registration})
    else:
        registration_form = RegistrationForm()
        return render(request, 'registration.html', {'registration_form': registration_form})


def thankyou(request):
    return render(request, 'thankyou.html', {})
