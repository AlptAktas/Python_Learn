# list
list = [1, 2, 3, 4, 5]

#dictionary
dictionary = {
    "key": "value"
}

#set
set = {1, 2, 3, 4, 5}

#tuple
tuple = (1, 2, 3, 4, 5)

#string
string = "Hello"

#integer
integer = 123

#float
float = 123

#boolean
boolean = True

#None
none = None


programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

print(programming_dictionary["Bug"])

programming_dictionary["Test"] = "The action of doing something over and over again"

print(programming_dictionary)


for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Key: [List]
# Key2: {Dictionary}

capitasl = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

print(travel_log["France"][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
    }
}

print(travel_log["France"]["cities_visited"][0])