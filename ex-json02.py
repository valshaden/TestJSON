from json import dumps, loads

json_string = '{"name" : "Джон", "возраст" : 36, "kids" : ["Mike", "Anna"], "pets" : {"dog" : "Rex", "cat" : "Barsik"}, "wife" : {"name" : "Jane", "age" : 6}}' #json-строка
print(json_string)
json_obj = loads(json_string) #создаем объект из строки
print(json_obj)
json_string = dumps(json_obj, indent=4, ensure_ascii=False) #создаем строку из объекта
print(json_string)

open("json_file.json", "w").write(json_string) #записываем строку в файл

json_string = open("json_file.json").read() #читаем строку из файла