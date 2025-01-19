resource_values = {
    "Water": 100,
    "Milk": 50,
    "Coffee": 76,
    "Money": 2.5,
}

def report():
    print(
        f"Water: {resource_values['Water']}ml\n"
        f"Milk: {resource_values['Milk']}ml\n"
        f"Coffee: {resource_values['Coffee']}g\n"
        f"Money: ${resource_values['Money']}"
    )

def is_enough(simple_resource_values):
    errors = []

    for key in simple_resource_values.keys():
        if simple_resource_values[key] <= resource_values[key]:
            continue
        else:
            print(f"There are not enough {key}.")
            errors.append(f"There are not enough {key}.")

    return errors

def money():
    1

def make_esppresso():
    simple_resource_values = {
        "Water": 20,
        "Milk": 0,
        "Coffee": 40,
        "Money": 0.5,
    }
    
    x = is_enough(simple_resource_values)
    return x, simple_resource_values

def make_latte():
    simple_resource_values = {
        "Water": 10,
        "Milk": 25,
        "Coffee": 40,
        "Money": 0.5,
    }
    
    x = is_enough(simple_resource_values)
    return x, simple_resource_values

def make_cappucino():
    simple_resource_values = {
        "Water": 10,
        "Milk": 40,
        "Coffee": 40,
        "Money": 0.5,
    }
    
    x = is_enough(simple_resource_values)
    return x, simple_resource_values

def get_user_choice():
    """Function to get user choice."""

    while True:
        user_choice = input(f"What would you like? (espresso/latte/cappucino): ").lower()
        if user_choice not in function_dic:
            print(f"You entered wrong input. Pls try again.")
            continue
        break

    return user_choice

def exit_state():
    """Function to get user exit choice."""

    coffee_machine_state = "on"
    while True:
        exit_state = input(f"Do you want to continue? (y/n): ").lower()

        if exit_state == "y":
            break
        elif exit_state == "n":
            coffee_machine_state = "off"
            break
        else:
            print("You entered wrong input. Pls try again.")
    
    return coffee_machine_state



function_dic = {
    "report": report,
    "espresso": make_esppresso,
    "latte": make_latte, 
    "cappucino": make_cappucino
}


while True:

    report()
    # get user choice for coffee type.
    user_choice = get_user_choice()

    # call the function from dictionary.
    if user_choice == list(function_dic.keys())[0]:
        function_dic[user_choice]()
    else: 
        errors, choice_resources = function_dic[user_choice]()
        if len(errors) > 0:
            break
        

        for key in resource_values:
            resource_values[key] -= choice_resources[key]
            
        
        print(f"Here is your {user_choice}!")
            
    

    # check if user wants to exit.
    if exit_state() == "off":
        break

    
    


   

