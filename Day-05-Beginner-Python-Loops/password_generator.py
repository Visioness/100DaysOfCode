import random
import string
import timeit

def my_function():
    letters = 5 # int(input("Welcome to the Password Generator MK.I\nHow many letters would you like in your password?\n"))
    symbols = 5 # int(input("How many symbols would you like in your password?\n"))
    numbers = 5 # int(input("How many numbers would you like in your password?\n"))

    generator = {"letters": letters, "symbols": symbols, "numbers":numbers}
    password = ""
    for _ in range(letters + symbols + numbers):
        for i in list(generator):
            if generator[i] == 0:
                del generator[i]
        choice = random.choice(list(generator))
        if choice == "letters":
            nextchar = random.choice(string.ascii_letters)
            generator["letters"] -= 1
        elif choice == "symbols":
            nextchar = random.choice(string.punctuation)
            generator["symbols"] -= 1
        elif choice == "numbers":
            nextchar = random.choice(string.digits)
            generator["numbers"] -= 1
        password += nextchar
    print("Your password 1 is:", password)


def angela_function():
    letters = 5 #int(input("Welcome to the Password Generator MK.I\nHow many letters would you like in your password?\n"))
    symbols = 5 #int(input("How many symbols would you like in your password?\n"))
    numbers = 5 #int(input("How many numbers would you like in your password?\n"))

    password = []
    for char in range(letters):
        password.append(random.choice(string.ascii_letters))
    for char in range(symbols):
        password.append(random.choice(string.punctuation))
    for char in range(numbers):
        password.append(random.choice(string.digits))
    
    passwordn = ""
    random.shuffle(password)
    for char in password:
        passwordn += char

    print("Your password 2 is:", passwordn)

def create_password():
    letters = 5 #int(input("Welcome to the Password Generator MK.I\nHow many letters would you like in your password?\n"))
    symbols = 5 #int(input("How many symbols would you like in your password?\n"))
    numbers = 5 #int(input("How many numbers would you like in your password?\n"))

    password_letters = [random.choice(string.ascii_letters) for char in range(letters)]
    password_symbols = [random.choice(string.punctuation) for char in range(symbols)]
    password_numbers = [random.choice(string.digits) for char in range(numbers)]
    
    password_all = []
    password_all = password_letters + password_numbers + password_symbols

    random.shuffle(password_all)
    final_password = "".join(password_all)

    print("Your password 3 is:", final_password)

time3 = timeit.timeit(create_password, number=100)
time2 = timeit.timeit(angela_function, number=100)
time1 = timeit.timeit(my_function, number=100)

print(f"Code 1 time: {time1}, Code 2 time: {time2}, Code 3 time: {time3}")