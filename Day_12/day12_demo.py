# global scope
enemies = 1

# local scope
def increase_enemies():
    global enemies # avoid changing global variables
    enemies = 2
    print(f"enemies inside function: {enemies}")


def increase_enemies1(enemies):
    return enemies + 1

increase_enemies()
increase_enemies1(enemies)

print(f"enemies outside function: {enemies}")