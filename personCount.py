# takes a JSON file and returns values based on the number of people
import json
from send import sendEmail
from interpreter import JSONtoEvent



def greaterThanMin(j: json):
    jParsed = json.loads(j)
    if len(jParsed["Participants"]) >= int(jParsed["min"]):
        sendEmail(JSONtoEvent(j))
        return True
    else:
        return False


def lessThanMax(j: json):
    jParsed = json.loads(j)
    if len(jParsed["Participants"]) <= int(jParsed["max"]):
        return True
    else:
        return False

x =  '{ "min":5, "max": 10, "Location":"Hills Field", "Time":"2:30", "Description":"Practice", "Title":"Prac", "Participants":[{"Name":"Jake", "Email":"frisboysproject@gmail.com"},{"Name":"Jordy", "Email":"jordypg@gmail.com"}]}'
print(greaterThanMin(x))
print(lessThanMax(x))