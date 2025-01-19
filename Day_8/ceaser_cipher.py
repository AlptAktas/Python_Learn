alpphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    shifted_text = ""

    if direction == "decode":
        shift *= -1
    
    for letter in text:
        if letter not in alpphabet:
            shifted_text += letter
        new_position = (alpphabet.index(letter) + shift) % len(alpphabet)
        shifted_text += alpphabet[new_position]

    
    return shifted_text



# def encrypt(text, shift):
#     shifted_text = ""

#     for letter in text:
#         new_position = (alpphabet.index(letter) + shift) % len(alpphabet)
#         shifted_text += alpphabet[new_position]
    
#     print(f"The encoded text is {shifted_text}")
    
#     return shifted_text

# def decrypt(text, shift):
#     original_text = ""

#     for lettter in text:
#         new_position = (alpphabet.index(lettter) - shift) % len(alpphabet)
#         original_text += alpphabet[new_position]
    
#     print(f"The decoded text is {original_text}")
    
#     return original_text



while True:

    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    user_text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shifted_text = caesar(user_text, shift, choice)

    print(f"Here is the {choice} result: {shifted_text}")

    user_choice = input("Do you want to go again? Type 'yes' or 'no':\n").lower()

    if user_choice == "no":
        break


# if choice == "encode":
#     shifted_text = encrypt(user_text, shift)
# elif choice == "decode":
#     original_text = decrypt(user_text, shift)
# else:
#     print("Invalid input")

