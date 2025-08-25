from json import dumps, loads
from json import dump, load

json_string = '{"name" : "Джон", "возраст" : 36, "kids" : ["Mike", "Anna"], "pets" : {"dog" : "Rex", "cat" : "Barsik"}, "wife" : {"name" : "Jane", "age" : 6}}' #json-строка

# print(json_string)
# json_obj = loads(json_string) #создаем объект из строки
# print(json_obj)
# json_string = dumps(json_obj, indent=4, ensure_ascii=False) #создаем строку из объекта
# print(json_string)

with open("data.json", "w", encoding="utf-8") as file:
    dump(json_obj, file, indent=4, ensure_ascii=False) #записываем объект в файл)
    print("Запись в файл произведена успешно")

