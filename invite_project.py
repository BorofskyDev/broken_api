import requests
import pprint
import json
raw_data = requests.get('https://ct-mock-tech-assessment.herokuapp.com/')
data = raw_data.json


class Country:
    _list = []

    def __init__(self, name):
        self.name = name
        self.people = []
        self._list.append(self)
        self.open_dates = {}
        self.conference_date = None
    
    @classmethod
    def find(cls, name):
        for place in cls.list:
            if place.name == name:
                return place
        return None
    
    def add_person(self, person):
        self.people.append(person)
    
    #need to attach availability to person. 
    def find_date(self):
        pass

class Person:
    _list =[]

    def __init__(self, name, email, country, dates):
        self.name = name
        self.email = email
        self.country = country
        self.dates = [ConferenceDate(date) for date in dates]
        self._list.append(self)

    def available_dates(self):
        open_dates = []
        pass

class ConferenceDate:
    def __init__(self):
        pass

    
#need a function to compare available dates 
    #function that pulls in the dates
    def something(self):
        pass 
    
    def moreSomething(self):
        pass
class Conference:
    _list = []

    def __init__(self, country):
        self.attendees = country.conference_date.attending
        self.attendees_num = len(self.attendees)
        self.name = country.name
        self.final_date = country.conference_dates
        self._list.append(self)
    
    def show(self):
        print(f'Country: {self.name}')
        print(f'Attendee Count: {self.attendee_count}')
        print(f'Start Date: ') #some code here to refer back to the start date of the conference
        print (f'Attendee Email Contact: {self.emails}')

conference_data = []
pass