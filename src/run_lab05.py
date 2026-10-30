import sys
sys.path.insert(0, ".")

from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx
import os

# Создаем папку out, если ее нет
os.makedirs("data/out", exist_ok=True)

# Выполняем конвертации
json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")
csv_to_xlsx("data/samples/cities.csv", "data/out/cities.xlsx")

print("Все файлы успешно созданы в data/out/!")