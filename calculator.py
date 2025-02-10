def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")

def add(a, b):
    return f"Wynik dodawania to {a} + {b} = {a + b}"

def subtract(a, b):
    return f"Wynik odejmowania to {a} - {b} = {a - b}"

def divide(a, b):
    if b == 0:
        return "Nie wolno dzielić przez 0"
    return f"Wynik dzielenia to {a} / {b} = {a / b}"

def multiply(a, b):
    return f"Wynik mnożenia to {a} * {b} = {a * b}"


operations = {
    '1': add,
    '2': subtract,
    '3': divide,
    '4': multiply
}

def menu():
    print("Witaj masz do wyboru 4 opcje działań:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Dzielenie")
    print("4. Mnożenie")

    x = input("Wybierz opcję (1-4): ")
    if x not in operations:
        print("Błąd: Niepoprawny wybór. Wybierz ponownie.")
        return

    a = get_number("Wybierz pierwszą liczbę: ")
    b = get_number("Wybierz drugą liczbę: ")

    print(operations[x](a, b))

menu()