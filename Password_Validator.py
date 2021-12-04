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
    print("""\n\033[4mPassword Requirements\033[0m
    Your password should have:
        \033[3m\033[93mAtleast 15 characters\033[0m
        \033[3m\033[94mAtleast one uppercase letter\033[0m
        \033[3m\033[35mAtleast one number\033[0m
        \033[3m\033[92mAtleast one special character (!#$%&()*+,-./:;<=>?@[\]^_{|}~)\033[0m
    """)
    specialSymbol = '$' '@' '#' '!' '%' '&' '(' ')' '*' '+' ',' '-' '.' ';' '/' ':' '<' '=' '>' '?' '[' ']' '^' '_' '{' '|''}' '~'
    while True:
        try:
            password = input("\033[31m\033[47mPlease enter a password: ")
        except ValueError:
            print("Password Invalid")
        if len(password) == 0:
            print("Password is empty")
        else:
            break

    
password()