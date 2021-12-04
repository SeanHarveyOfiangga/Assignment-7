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

#intro
def intro():
    print("\n\033[47m\033[30m**Welcome to password validator app!**\033[0m")
intro()

#password validator function
def password():
    print("""\n\033[4mPassword Requirements\033[0m
    Your password should have:
        \033[3m\033[93mAtleast 15 characters\033[0m
        \033[3m\033[92mAtleast one uppercase letter\033[0m
        \033[3m\033[35mAtleast one number\033[0m
        \033[3m\033[94mAtleast one special character (!#$%&()*+,-./:;<=>?@[\]^_{|}~)\033[0m
    ********************************************************************""") #docstring for password requirements
    #special characters variable
    specialchar = '$' '@' '#' '!' '%' '&' '(' ')' '*' '+' ',' '-' '.' ';' '/' ':' '<' '=' '>' '?' '[' ']' '^' '_' '{' '|''}' '~'
    while True:
        passwordvalidity = True
        try:
            password = input("\n\033[32mPlease enter a password: \033[0m")  #input
        except ValueError:
            print("\033[31mPassword Invalid")       #value error validation
        if len(password) == 0:
            print("\033[31mPassword is empty\033[0m")       #checks if the password is empty or not
            passwordvalidity = False
        if len(password) < 15:
            print("\033[31mPassword is too short\033[0m")   #checks if the password is short or not
            passwordvalidity = False
        if not any(character.isupper() for character in password):
            print("\033[31mPassword should have atleast one uppercase letter\033[0m")       #checks if the password has atleast one uppercase letter or not
            passwordvalidity = False
        if not any(character.isdigit() for character in password):
            print("\033[31mPassword should have atleast one number\033[0m")     #checks if the password has atleast one number
            passwordvalidity = False
        if not any(character in specialchar for character in password):
            print("\033[31mPassword should have atleast one special character\033[0m")  #checks if the password has atleast one special character
            passwordvalidity = False
        elif passwordvalidity == True:
            print("\n\033[42m\033[30mPassword is valid\033[0m")     #if the password is valid this condition will apply
            print("\nThank you for using the password validator app!")
            exit()

#call for the function  
password()