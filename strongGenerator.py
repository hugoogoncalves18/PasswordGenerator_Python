import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

user_input = input("Number of characters: ")

while True:
    try:
        character_number = int(user_input)

        if character_number < 12:
            print("Your number should be at least 12")

            user_input = input("Please enter a new number: ")
        else:
            break
    except:
        print("Please, Enter a numbers only.")

        user_input =input("Number of characters: ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(character_number * (30/100))
part2 = round(character_number * (20/100))

result=[]

for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])
for x in range(part2):
    result.append(s3[x])
    result.append(s4[x])

random.shuffle(result)

password = "".join(result)
print("Strong password: ", password)