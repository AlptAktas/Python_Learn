# Errors, Exceptions and JSON Data: Improving the Password


# KeyError, IndexError, TypeError


# try:
#     file = open("Day_30/a_file.txt")
# except Exception as e:
#     print(f"{e}: I created the file for you :)")
#     open("Day_30/a_file.txt", "w")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height **2
print(bmi)