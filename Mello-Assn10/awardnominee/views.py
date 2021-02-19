# Create your views here.
from django.shortcuts import render
from awardnominee.models import AwardNominee
from awardnominee.forms import AwardForm


def awards(request):
    person1 = AwardNominee.objects.get(id="1")
    person2 = AwardNominee.objects.get(id="2")
    person3 = AwardNominee.objects.get(id="3")
    if request.method == 'post':
        award_form = AwardForm(request.POST)
        if award_form.is_valid():
            award_form.save(commit=True)
            new_award = award_form.cleaned_data
            return render(request, 'awards.html', {'award_form': new_award,'bill': person1, 'chris': person2, 'jake': person3})
    else:
        award_form = AwardForm()
        return render(request, 'awards.html', {'award_form': award_form, 'bill': person1, 'chris': person2, 'jake': person3})
