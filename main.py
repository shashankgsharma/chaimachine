from chai import MENU, resources
from os import system


# TODO 3: print report
def format_report(money):
    print("Report: ")
    print(f"\twater: {resources['water']} ml")
    print(f"\tmilk: {resources['milk']} ml")
    print(f"\ttea leaves: {resources['chai patti']} gm")
    print(f"\tMasala: {resources['masala']} gm")
    print(f"\tGinger: {resources['ginger']} gm")
    print(f"\tcardamom: {resources['cardamom']}")
    print(f"\tearned money: ₹{money}")


# TODO 4: check resources sufficient?
def check_resources(choice):
    if choice not in MENU:
        print("Please select from the given options only!")
        return False
    for ingredient in MENU[choice]["ingredients"]:
        if resources[ingredient] - MENU[choice]["ingredients"][ingredient] >= 0:
            resources[ingredient] -= MENU[choice]["ingredients"][ingredient]
            return True
        else:
            print(f"Sorry, there's not enough {ingredient}!")
            return False


# TODO 5: Process coins, check transaction
def check_transaction(coins1, coins2, coins5, coins10, choice):
    user_sum = (1 * coins1) + (2 * coins2) + (5 * coins5) + (10 * coins10)
    if user_sum < MENU[choice]["cost"]:
        print("Sorry, That's not enough money!")
        refund = user_sum
        print(f"Your ₹{refund} is refunded.")
        return 0
    change = user_sum - MENU[choice]["cost"]
    if choice == 'm':
        tea = "masala tea"
    elif choice == 'g':
        tea = "gingerly tea"
    elif choice == 'c':
        tea = "cardamom tea"
    else:
        return print("There is a bug!")
    print(f"Here is ₹{change} in change.\nHere is your {tea}🍵, Enjoy!")
    return MENU[choice]["cost"]


# TODO 6: Make chai
def make_chai():
    machine_on = True
    money = 0

    while machine_on:
        # TODO 1: Prompt User by asking "What would you like?"(masala chai/ gingerly chai/ cardamom chai):
        choice = input("Hello, what would you like to have? (masala tea 'm'/ gingerly tea 'g'/ cardamom tea 'c'): ").lower()
        system('clear')

        if not choice.isalpha():
            print("Please answer only in english alphabets!")
        # TODO 2: Turn off the chai machine by entering "off" the prompt
        elif choice == "off":
            system('clear')
            machine_on = False
            print("Thanks for using our chai🍵 services.\nDo come again, Goodbye!")

        elif choice == "report":
            format_report(money)

        else:
            resources_available = check_resources(choice)
            if resources_available:
                print("Insert coins: ")
                correct_ans = False
                while not correct_ans:
                    coins1 = input("\t₹1 coins: ")
                    coins2 = input("\t₹2 coins: ")
                    coins5 = input("\t₹5 coins: ")
                    coins10 = input("\t₹10 coins: ")
                    if coins1.isnumeric() and coins2.isnumeric() and coins5.isnumeric() and coins10.isnumeric():
                        correct_ans = True
                        coins1 = int(coins1)
                        coins2 = int(coins2)
                        coins5 = int(coins5)
                        coins10 = int(coins10)
                        system('clear')
                        money += check_transaction(coins1, coins2, coins5, coins10, choice)

                    else:
                        system('clear')
                        print("Please enter whole number values only to the number of coins.")


make_chai()
