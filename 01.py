# Общая сумма расходов
import json
from json import dumps, loads, dump

with open('task01.json', encoding='utf-8') as file:
    data = json.load(file)
    print(data)

total_sum = sum(item['сумма'] for item in data)
print(total_sum)

cats = {}
for item in data:
    if item["категория"] in cats:
        cats[item["категория"]] += item["сумма"]
    else:
        cats[item["категория"]] = item["сумма"]
   
#  Категория с наибольшими тратами    
print (cats)
max_category = max(cats, key=cats.get)  
print(max_category)

print(cats)
