list_pokupok = ["молоко", "хліб", "масло", "м'ясо", "картопля"]
list_pokupok.append("сир")

list_marks = [8, 9, 10, 9, 9, 10, 11]
sr_ar = sum(list_marks) / len(list_marks)

list_names = ["Свят", "Саша", "Настя", "Вова" , "Таня", "Галя", "Соломон"]
list_names.sort()
print(list_names)

list_city = ["Запоріжжя", "Дніпро", "Черкаси", "Київ", "Миколаів"]
list_city[1]="Одеса"
print(list_city[1], list_city[-1])

list_predmeti = ["Математика", "Література", "Фізика", "Хімія", "Інформатика"]
print(len(list_predmeti))
list_predmeti.remove("Література")
list_predmeti.reverse()