#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Day_24/MailMergeProjectStart/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    invited_guest = names_file.readlines()


with open("Day_24/MailMergeProjectStart/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    starting_letter = letter_file.read()
    for name in invited_guest:
        stripped_name = name.strip()
        new_letter = starting_letter.replace("[name]", stripped_name)
        with open(f"Day_24/MailMergeProjectStart/Mail Merge Project Start/Output/Letter_for_{stripped_name}.docx", "w") as output:
            output.write(new_letter)
