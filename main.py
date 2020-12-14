#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.docx", mode="r") as file:
    letter_body = file.read()

with open("./Input/Names/invited_names.txt", mode="r") as file:
    invitees = file.read().splitlines()

list_of_names = []
for name in invitees:
    list_of_names.append(name.replace("\n", ""))

for name in list_of_names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.docx", mode="w") as file:
        file.write(letter_body.replace("[name]", name))