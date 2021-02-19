from django.forms import ModelForm
from registration.models import Workshop


class WorkshopForm(ModelForm):
    class Meta:
        model = Workshop
        fields = [
            'title',
            'session',
            'room',
            'start',
            'end'
        ]
