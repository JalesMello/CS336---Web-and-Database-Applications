from django.forms import ModelForm, Select
from registration.models import Registrant


class RegistrationForm(ModelForm):
    TITLE_CHOICES = (
        ('MR', 'Mr.'),
        ('MS', 'Ms.'),
        ('MRS', 'Mrs.'),
        ('SR', 'Sr.'),
        ('JR', 'Jr.'),
    )
    MEALS_CHOICES = (
        ('mealpack', 'Meal Pack'),
        ('dinnerday2', 'Dinner Day 2'),
    )
    SESSION1_CHOICES = (
        ('Workshop_A', 'Workshop A'),
        ('Workshop_B', 'Workshop B'),
        ('Workshop_C', 'Workshop C'),
    )
    SESSION2_CHOICES = (
        ('Workshop_D', 'Workshop D'),
        ('Workshop_E', 'Workshop E'),
        ('Workshop_F', 'Workshop F'),
    )
    SESSION3_CHOICES = (
        ('Workshop_G', 'Workshop G'),
        ('Workshop_H', 'Workshop H'),
        ('Workshop_I', 'Workshop I'),
    )
    CARD_TYPE_CHOICES = (
        ('MC', 'Mastercard'),
        ('V', 'Visa'),
        ('AE', 'American Express'),
    )

    class Meta:
        model = Registrant
        fields = [
            'title',
            'firstname',
            'lastname',
            'street_address_1',
            'street_address_2',
            'city',
            'state',
            'zipcode',
            'telephone',
            'email',
            'company',
            'website',
            'position',
            'meals',
            'session1',
            'session2',
            'session3',
            'billing_firstname',
            'billing_lastname',
            'card_type',
            'exp_year',
            'exp_month'
        ]

    widgets = {
        'title':
            Select(choices=TITLE_CHOICES),
        'meals':
            Select(choices=MEALS_CHOICES),
        'session1':
            Select(choices=SESSION1_CHOICES),
        'session2':
            Select(choices=SESSION2_CHOICES),
        'session3':
            Select(choices=SESSION3_CHOICES),
        'card_type':
            Select(choices=CARD_TYPE_CHOICES),
    }
