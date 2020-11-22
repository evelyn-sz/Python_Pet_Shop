# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop_name):
    return pet_shop_name["name"]

def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]

def add_or_remove_cash(total_cash, number):
    number = 10
    total_cash["admin"]["total_cash"] += number



# def total_money(people_dictionaries):
#     money = 0
#     for person in people_dictionaries:
#         money += person['monies']
#     return money

    
# #7

# def l_money(ler, lee, amount):
#     ler['monies'] -= amount
#     lee["monies"] += amount
#     # print (ler["monies"])
#     # print (lee["monies"])