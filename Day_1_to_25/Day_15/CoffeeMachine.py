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
}
deposit= 0.0
machine = "on"
print("Welcome to Cafeinated ☕")
while(machine == "on"):

    order = input("What would you like to have today? Espresso(1.5), Latte(2.5) or Cappuccino(3.0)? ").lower()

    if order == "off":
        machine = "off"
    if order == "report":
        for resource in resources:
            print(f"{resource.title()} : {resources[resource]}")
        print(f"Money: ${deposit}")
        continue

    for i in resources:
        if resources[i] < MENU[order]["ingredients"][i]:
            print("Not enough resources.")
            exit()

    pennies = int(input("Enter number of pennies: "))
    nickles = int(input("Enter number of nickles: "))
    dimes = int(input("Enter number of dimes: "))
    quarters = int(input("Enter number of quarters"))
    amount_entered = (pennies*0.01)+(nickles*0.05)+(dimes*0.1)+(quarters*0.25)
    if amount_entered < MENU[order]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        continue
    elif amount_entered == MENU[order]["cost"]:
        print("Preparing your Drink . . . ")
        deposit += amount_entered
    else:
        print(f"Here's ${amount_entered-MENU[order]['cost']} in change.")

    for item in resources:
        resources[item]-=MENU[order]["ingredients"][item]


    print(f"Here's your {order}. Enjoyy!")




