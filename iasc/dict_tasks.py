# Завдання 1 – Телефонна книга
contacts = {
    "Anna": "093-123-45-67",
    "Ivan": "050-888-99-00",
    "Olha": "097-777-33-22"
}
contacts["Taras"] = "063-000-11-22"
del contacts["Ivan"]
names = list(contacts)
print(names)        # ['Anna', 'Olha', 'Taras']
tel_numbers = list(contacts.values())
print(tel_numbers)        # ['093-123-45-67', '097-777-33-22', '063-000-11-22']
if "Katya" in tel_numbers:
    print("Ключ Katya міститься у словнику")
else:
    print("Ключ Katya відсутен у словнику")

#   Завдання 2 – Оцінки по предметах
grades = {
    "math" : 88,
    "physics" : 75,
    "english" : 93,
    "history" : 59
    }
balls = grades.values()
max_ball=max(balls)
predmet_max_ball = [k for k, v in grades.items() if v == max_ball]
print(predmet_max_ball) #['english']
sr_ball=sum(balls)/len(balls)   #78.75
list_predmet_ball80 = [k for k, v in grades.items() if v > 80]
print(list_predmet_ball80) #['math', 'english']

# Завдання 3 – Рахунок клієнтів
transactions = [
    ("Anna", 200),
    ("Ivan", -50),
    ("Anna", 100),
    ("Olha", 500),
    ("Ivan", 150),
    ("Olha", -100),
]
unique_transactions_sums = {}
for name, amount in transactions:
    unique_transactions_sums[name] = unique_transactions_sums.get(name, 0) + amount
print(unique_transactions_sums) #{'Anna': 300, 'Ivan': 100, 'Olha': 400}
client_max_balance = max(unique_transactions_sums, key=unique_transactions_sums.get)
print(client_max_balance )
result=False
for name, sum_balance in unique_transactions_sums.items():
    if sum_balance < 0:
        print(f"{name}: {sum_balance} грн")
        result=True
if result==False:
    print("Кліенти з від’ємним балансом відсутні")

# Завдання 4 – Підрахунок слів
text = "hello world hello again hello world test world"
words_list = text.split()
words_number = {}
for word in words_list:
    words_number[word] = words_number.get(word, 0) + 1
print(words_number)

#Завдання 5 – JSON: словник у рядок
student = {
    "name": "Anna",
    "age": 20,
    "courses": ["math", "physics", "english"]
}
#– Імпортуйте модуль json
import json
#– Перетворіть словник у JSON-рядок і виведіть його
json_string_student = json.dumps(student, ensure_ascii=False)
print(json_string_student)
#– Знову перетворіть цей рядок у словник
dict_student2=json.loads(json_string_student)
#– Додайте курс "history" до списку courses
student["courses"].append("history")
print(student)