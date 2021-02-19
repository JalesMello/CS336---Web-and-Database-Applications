import json
from registration.models import Registrant

try:
    with open('data/registrant_data.json', 'r') as inputFile:
        allRegistrants = json.load(inputFile)
        for registrant in allRegistrants['registrants']:
            newRegistrant = Registrant()
            for key in registrant:
                newRegistrant.__dict__[key] = registrant[key]
            newRegistrant.save()
except OSError as err:
    print("No input file found")
