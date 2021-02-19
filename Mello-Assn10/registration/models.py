from django.db import models


# Create your models here.
class Registrant(models.Model):
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
        ('Workshop A', 'Workshop A'),
        ('Workshop B', 'Workshop B'),
        ('Workshop C', 'Workshop C'),
    )
    SESSION2_CHOICES = (
        ('Workshop D', 'Workshop D'),
        ('Workshop E', 'Workshop E'),
        ('Workshop F', 'Workshop F'),
    )
    SESSION3_CHOICES = (
        ('Workshop G', 'Workshop G'),
        ('Workshop H', 'Workshop H'),
        ('Workshop I', 'Workshop I'),
    )
    CARD_TYPE_CHOICES = (
        ('MC', 'Mastercard'),
        ('V', 'Visa'),
        ('AE', 'American Express'),
    )
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    date_of_registration = models.DateField(auto_now_add=True)
    street_address_1 = models.CharField(max_length=60)
    street_address_2 = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    telephone = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    website = models.CharField(max_length=60)
    position = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    meals = models.CharField(max_length=30, choices=MEALS_CHOICES)
    billing_firstname = models.CharField(max_length=30)
    billing_lastname = models.CharField(max_length=30)
    card_type = models.CharField(max_length=16, choices=CARD_TYPE_CHOICES)
    card_csv = models.CharField(max_length=4)
    exp_year = models.CharField(max_length=4)
    exp_month = models.CharField(max_length=2)
    session1 = models.CharField(max_length=35, choices=SESSION1_CHOICES)
    session2 = models.CharField(max_length=35, choices=SESSION2_CHOICES)
    session3 = models.CharField(max_length=35, choices=SESSION3_CHOICES)


class Workshop(models.Model):
    title = models.CharField(max_length=40)
    session = models.CharField(max_length=10)
    room = models.CharField(max_length=10)
    start = models.CharField(max_length=10)
    end = models.CharField(max_length=10)
