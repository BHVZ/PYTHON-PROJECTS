import random
import string

length = int(input("ENTER PASSWORD LENGTH: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = " "

for i in range(length):
    password += random.choice(characters)

print("YOUR PASSWORD IS: ",password)
