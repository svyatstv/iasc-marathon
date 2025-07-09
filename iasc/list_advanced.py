#  Завдання 1 - Аналіз оцінок по студентах
students = ["Anna", "Ivan", "Olha", "Taras", "Katya"]
grades = [95, 62, 47, 88, 53]
max_grade=max(grades)
ind_max=grades.index(max_grade)
num_nezdali=0
list_zdali = []
for i in range(len(grades)):
    if grades[i]>60:
        list_zdali.append(students[i])
    else:
        num_nezdali=num_nezdali+1
print(students[ind_max])  
print(list_zdali)
print(num_nezdali)     

# Завдання 2 - Статистика по повідомленнях
logs = ["ok", "error", "fail", "ok", "error", "warning", "ok", "fail"]
unique_logs = set(logs)
nums_logs = []
for item in unique_logs:
    nums_logs.append(logs.count(item))

nums_error=logs.count("error")/len(logs)*100
#print(unique_logs)
#print(nums_logs)
print(nums_error)

# Завдання 3 - Витрати за тиждень
expenses = [
    ["Понеділок", 120],
    ["Вівторок", 80],
    ["Середа", 150],
    ["Четвер", 0],
    ["П’ятниця", 250],
    ["Субота", 300],
    ["Неділя", 200]
]
max_day_trati = 0
week_trati = 0
list_sverhtrati = []
for element in expenses:    
    trati = element[1]
    week_trati=week_trati+trati
    if trati>max_day_trati:
        max_day_trati=trati
    if trati>100:
        list_sverhtrati.append(element[0])

print(max_day_trati)
print(week_trati)
print(list_sverhtrati)

# Завдання 4 - Робота з вкладеними списками
products = [
    ["яблуко", 2, 12.5],
    ["банан", 5, 8.0],
    ["молоко", 1, 34.0],
    ["хліб", 2, 16.0]
]
sum = 0
max_expensiev = 0
name_expensiev=0
products_expenses = []
for element in products:
    sum=sum+element[1]*element[2]
    if element[2]>max_expensiev:
        max_expensiev=element[2]
        name_expensiev=element[0]
    products_expenses.append([element[0],element[1]*element[2]])
#print(sum)
#print(name_expensiev)
#print(products_expenses)

# Завдання 5 —-Генератор квадратів з умовою
squares = [x*x for x in range(30) if x % 2 == 0 and x % 4 != 0 and x not in [10, 14, 18]]
#print(squares)