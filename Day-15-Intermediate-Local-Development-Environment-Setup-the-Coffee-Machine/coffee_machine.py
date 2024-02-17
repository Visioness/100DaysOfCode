COFFEES = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappucino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    }
}

report = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0,
}


def main():
    while True:
        task = input("What would you like? ('espresso' for Espresso / 'latte' for Latte / 'cappucino' for Cappucino) : ")
        while task not in ["espresso", "cappucino", "latte", "report"]:
            task = input("What would you like? ('espresso' for Espresso / 'latte' for Latte / 'cappucino' for Cappucino) : ")
        
        if task == "report":
            print(f"Water: {report['water']}ml\nCoffee: {report['coffee']}gr\nMilk: {report['milk']}ml\nMoney: ${report['money']}")  
        else:
            print(make_coffee(task))


def insert_coins():
    try:
        quarters = int(input("Please insert the coins.\nHow many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))

        coins = (quarters * 25 + dimes * 10 + nickels * 5 + pennies * 1) / 100.0
        return coins
    except ValueError: 
        insert_coins()


def make_coffee(coffee):
    for ingredient in COFFEES[coffee]["ingredients"]:
        if report[ingredient] < COFFEES[coffee]["ingredients"][ingredient]:
            return f"Not enough {ingredient} in the coffee machine!"
    
    coins = insert_coins()

    if COFFEES[coffee]["cost"] <= coins:
        for ingredient in COFFEES[coffee]["ingredients"]:
            report[ingredient] -= COFFEES[coffee]["ingredients"][ingredient]
        report["money"] += COFFEES[coffee]["cost"]

        result = f"Here is ${(coins - COFFEES[coffee]['cost']):.2f} in change.\nHere is your {coffee}" if coins > COFFEES[coffee]["cost"] else f"Here is your {coffee}"
        return result

    else:
        return f"Not enough money. ${coins} refunded."
    

if __name__ == "__main__":
    main()