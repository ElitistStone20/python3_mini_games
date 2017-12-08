# ask user if they want to encrypt or decrypt
# get input
# if encrpypt is chosen then as k the user what they want to encrpypt
# ask the key they want to use
alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
def encrypt(msg, key):
    transformed = ""
    msg = str(msg)
    for i in msg:
        if i in alphabet:
            loc = alphabet.index(i)
            newloc = loc + key
            transformed += alphabet[newloc]
        elif i in numbers:
                loc = numbers.index(i)
                newloc = loc + key
                transformed += numbers[newloc]
        else:
            transformed += i
    print(transformed)

def decrypt(msg, key):
    transformed = ""
    msg = str(msg)
    for i in msg:
        if i in alphabet:
            loc = alphabet.index(i)
            newloc = loc - key
            transformed += alphabet[newloc]
        elif i in numbers:
                loc = numbers.index(i)
                newloc = loc - key
                transformed += numbers[newloc]
        else:
            transformed += i
    print(transformed)

def userInput():
    mode = input("Do you want to encrypt or decrypt your message? Please type e for encrypt and d for decrypt! ")
    return mode

def program(mode):
    try:
        msg = input("what message do you want to process? ").lower()
        key = int(input("What key are you going to use? "))
        if mode == "e":
            encrypt(msg, key)
        elif mode == "d":
            decrypt(msg, key)
        else:
            print("Please enter a valid command ")
            userInput()
    except ValueError:
        print("Something went wrong. Of cource!")

program(userInput())
