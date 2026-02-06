import random
import string

#Generate lenght
lenght = int(input("Enter a password lenght: "))

print("Choose character ser for password from these: \n1-Digits\n2-Characters\n3-Special characters\n4-Exit")

characterList=""

"Getting character set for password"

while(True):
    choice = int(input("Choice a option: "))

    if (choice == 1):
        characterList += string.ascii_letters
        break
    elif (choice == 2):
        characterList += string.digits
        break
    elif (choice == 3):
        characterList += string.punctuation
        break
    elif (choice == 4):
        print("Thank You, Bye")
        break
    else:
        print("Please pick a valid option")
    
password = []

for i in range(lenght):

    randomchar = random.choice(characterList)
    password.append(randomchar)

print("Your password: " + "".join(password))
