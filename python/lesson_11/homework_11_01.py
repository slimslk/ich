name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

string_1 = "Привет, меня зовут {0}. Мне {1} лет. Я живу в {2}.".format(name, age, city)
string_2 = f"Привет, меня зовут {name}. Мне {age} лет. Я живу в {city}."

print(string_1)
print(string_2)