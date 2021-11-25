import requests
import pprint
import json
r = requests.get('https://ct-mock-tech-assessment.herokuapp.com/').json()

pprint.pprint(r)

