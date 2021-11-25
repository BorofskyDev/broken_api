import requests
import pprint
import json
from datetime import date

# raw_data = requests.get('https://ct-mock-tech-assessment.herokuapp.com/')
# data = raw_data.json

#Order should go - Pull from API to get data. Once it has the data:
# 1) Sort everything by country
# 2) Sort people by country 
# 3) Pull the dates and compare them, find the ones that return with the most matches. 
# 4) Sort those who can make that country's conference from those that can't
# 5) Return a list that shows the Country, the conference date, and the email address of those who can attend 


pp=pprint.PrettyPrinter(indent=4)

class Person:
    def __init__(self, availableDates, country, email, firstName, lastName):
        self.availableDates = availableDates
        self.country = country
        self.email = email
        self.firName = firstName
        self.lastName = lastName


    @classmethod
    def open_dates(cls):
        cls.availability = []
        pass
    


class ConferenceLocation:
    #I need a list of countries that have been entered. This way if the country is in the list, when it gets
    #to the person they can just be added to the country. If it's scanning through the data and sees a person attached
    #to a country that doesn't exist, I need it to create a country for that person and automatically categorize it. 
    #This begins with a _list function.
    _list = []
    

    #What's needed to know about the country? I need to know the country name, the people attached to the country, a way to append my list, what dates are available for each country, and the final date
    #it's quicker to find available dates by country since each one will have its own conference. No reason to sift through available dates for people who won't attend the same conference
    def __init__(self, country):
        self.country = country
        self.people = []
        self._list.append = []
        self.available_dates = []
        self.conference_date = None

    @classmethod
    def find_country(cls, country):
        if cls._list:
            for c in cls._list:
                if country.title() != c.name:
                    cls._list.append(c.name)
        
        try:
            r = requests.get('https://ct-mock-tech-assessment.herokuapp.com/').json()
            for p in r['partners']:
                p = Person(p['availableDates'], p['country'], p['email'], p['firstName'], p['lastName'])
                cls._list.append(p)
                # cls.availability.append(p['availableDates'])
                # print(p.__dict__)
                # break
                print("successful")

        except:
            print("We could not connect to")
        
class ConferenceDate:
    pass


# class FinalConference:
#     _list = []

#     def __init__(self, country):
#         pass

print("c'mon")

