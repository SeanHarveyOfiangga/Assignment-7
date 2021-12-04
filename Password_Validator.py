#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex.
#input: P@ssw0rd+P@ssw0rd
#ouput: Valid

#Tip: loop through each character of the input then process it letter by letter

def intro():
    print("\n\033[47m\033[30m**Welcome to password validator app!**\033[0m")
intro()

def password():
    password = input("\n\033[92mPlease enter a password: \033[0m")
    print(password)

password()