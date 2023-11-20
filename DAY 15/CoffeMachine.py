from flask.scaffold import F

MENU = {
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
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "cost": 0
}


def report_resource():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} gr")
    print(f"Money: ${resources['cost']}")


def coin_operations():
    quarter = int(input("How many quarters? "))
    money_quarter = 0.25 * quarter
    dimes = int(input("How many dimes? "))
    money_dimes = 0.10 * dimes
    nickel = int(input("How many nickel? "))
    money_nickel = 0.05 * nickel
    pennies = int(input("How many Pennies? "))
    money_pennies = 0.01 * pennies
    cost = money_dimes + money_nickel + money_pennies + money_quarter
    return cost

def espresso():
    cost = coin_operations()
    cost = cost - MENU["espresso"]['cost']
    if cost < 0: 
        print("Sorry, you don't have enough money")    


def main():
    user_input = input("What would you like ? (espresso/latte/cappuccino): ")
    print("Please Insert Coin")
    
    if user_input == "report":
        report_resource()


main()
