from json import dumps, loads

json_string = '{"name" : "John", "age" : 36, kids = {"name" : "Jane", "age" : 6}}' #json string
print(json_string)

json_string = loads(json_string) #json string to python dictionary
print(json_string)

json_string = dumps(json_string) #python dictionary to json string
print(json_string)


