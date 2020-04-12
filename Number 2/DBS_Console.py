def char_split():
    # welcome message
    print("#########################\nWELCOME TO THE DBS CONSOLE\n#########################\n")
    # input username
    username = input("Please enter your username: ") 
   # Split when the program encounters the \ character
    domain = username.split('\\')[0]
    user_name = username.split('\\')[-1]
    print(f"\nDomain : {domain}\nUsername : {user_name}")


char_split()