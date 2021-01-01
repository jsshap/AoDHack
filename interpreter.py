#JSON interpreter which turns JSON file into an Event object
import json

x =  '{ "Location":"Hills Field", "Time":"2:30", "Description":"Practice", "Participants":[Jordy,Sung,Jake,Vaibhav,notGeorge]}'
def JSONtoEvent(j: json):
    parse = json.loads(j)
    print(parse)
    return parse
print(JSONtoEvent(x)["Time"])