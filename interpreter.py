#JSON interpreter which turns JSON file into an Event object
import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
def JSONtoEvent(j: json):
    parse = json.loads(j)
    print(parse)
    return parse
print(JSONtoEvent(x)["age"])