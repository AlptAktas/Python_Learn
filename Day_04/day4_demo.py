import random

# random_integer = random.randint(0, 100)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# random_float = random.uniform(0, 100)
# print(random_float)

random_heads_or_tails = random.randint(0, 1)

if random_heads_or_tails == 1:
    print("Heads")
else:
    print("Tails")

# random_choice = random.choice([1, 2, 3, 4, 5])
# print(random_choice)

# random_choice = random.choice("Hello")
# print(random_choice)

# list
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]

random_choice = random.choice(fruits)
print(random_choice)

random_choice = random.choices(fruits, k=2)
print(random_choice)

random_int = random.randint(0, len(fruits) - 1)
print(fruits[random_int])

x = [1, 2, 3, 4, fruits]
print(x[3])
print(x[4][2])
print(x[4])