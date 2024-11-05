import simplejson as json
import os

if os.path.isfile("newFile.txt") and os.stat("ages.json").st_size != 0:
    print("if statement")
    old_file = open("ages.json", "r+")
    data = json.loads(old_file.read())
    print("Current age is", data["age"], "---adding a year")
    data["age"] = data["age"] + 1
    print("New Age", data["age"])

else:
    print("else")
    try:
        old_file = open("ages.json", "w+")
    except IOError:
        print("File not found")
    else:
        data = {"name": "lucienne", "age": 32}
        print("The file found, setting default age", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))

#
# import json
#
# person = {
#      'first_name': "John",
#      "isAlive": True,
#      "age": 27,
#      "address": {
#          "streetAddress": "21 2nd Street",
#          "city": "New York",
#          "state": "NY",
#          "postalCode": "10021-3100"
#      },
#      "hasMortgage": None
# }
# with open('ages.json', 'w') as f:  # writing JSON object
#      json.dump(person, f)
# open('ages.json', 'r').read()   # reading JSON object as string
# '{"hasMortgage": null, "isAlive": true, "age": 27, "address": {"state": "NY", "streetAddress": "21 2nd Street", "city": "New York", "postalCode": "10021-3100"}, "first_name": "John"}'
#
#
# type(open('ages.json', 'r').read())


