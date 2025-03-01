import json

x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)  

print(y["age"])

import json

x = {"name": "John", "age": 30, "city": "New York"}
y = json.dumps(x)  

print(y)


json.dumps(x, indent=4)
json.dumps(x, indent=4, separators=(". ", " = "))
json.dumps(x, indent=4, sort_keys=True)


