# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")


# # greet()
# # greet_with_name("Angela")
# greet_with(location= "Jack Bauer", name= "Nowhere")



def calculate_love_score(*args):
    true_count = 0
    love_count = 0
    
    for name in args:
        for letter in name.lower():
            if letter in "true":
                true_count += 1
            if letter in "love":
                love_count += 1
    return int(f"{true_count}{love_count}")
    



print(calculate_love_score("Selinay", "Alptekin"))