from django import forms


class AwardForm(forms.Form):
    CHOICES = [
        ('A', 'Vote for Bill!'),
        ('B', 'Vote for Christina!'),
        ('C', 'Vote for Jake!'),
    ]
    vote = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
