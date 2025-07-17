#функція виводить “Hello, world!”
def hello_world():
    print("Hello, world!")
hello_world()

#функція вітає ім’ям
def greet(name):
    print(f'Привіт, {name}!')
greet("Anna")

#функція повертає квадрат числа
def square(a):
    return a*a
print(square(5))

#функція повертає суму
def add(a, b):
    return a+b   
print(add(5,4))
#функція  вітає навіть без параметра
def greet(name="Гість"):
    print(f'Привіт, {name}!')
greet("Anna")    
greet()   

#функція повертає n!
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n<0:
        return("Error")
    else:
        return n * factorial(n - 1)
print(factorial(3))

#функція повертає True, якщо парне
from typing import Callable
is_even: Callable[[int], bool] = lambda y: y % 2 == 0
print(is_even(2))

#функція виводить числа від 1 до n
def print_numbers(n):
    for i in range(1, n +1):
        print(i)
print_numbers(5)

#функція повертає True, якщо є в списку, та False коли немає в списку 
def find_name(name, name_list):
    return name in name_list
print(find_name("Anna", ["Svyat", "Anna", "Alex"]))
print(find_name("Anna", ["Svyat", "Ira"]))

#функція повертає найбільше з трьох
def max_of_three(a, b, c):
    return max(a, b, c)
print(max_of_three(3,7, 2))

#функція повертає рядок навпаки
def reverse_string(s):
    return s[::-1]
print(reverse_string("Привіт, як справи?"))

#функція рахує голосні 
def count_vowels(s):
    vowels = "аеоуиїієАОУИЇІЄЕ"
    return sum(1 for char in s if char in vowels)
print(count_vowels("Привіт"))

#функція повертає середнє значення 
def average(*numbers):
   if not numbers:
        return "ERROR"
   return sum(numbers) / len(numbers)
print(average(2,4,6))

#функція виводить name, age тощо
def print_user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
print_user_info(name="Svyat", age=13, city="Zaporizhzhye")

#функція outer(), яка викликає inner() - виводить “Я - вкладена функція!”
def outer():
    def inner():
        print("Я - вкладена функція!")
    inner()
outer()