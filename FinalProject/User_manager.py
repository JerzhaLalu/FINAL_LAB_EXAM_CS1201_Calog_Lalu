
user_database={}

class User_manager:
   
    def register():
        while True
            try:
                username = str(input("Enter your username:"))
                    if len(username) <= 4:
                        print ("Username must be 4 characters long. Try again")
                    else:
                        return
                    
                password = input("Enter your password: ")
                    if len(password)<=8:
                        print ("Username must be 8 characters long. Try again")
                    else:
                        return
            user_database[username]={"password":password}
         except ValueError as e:
            print(e)

    def login():
        while True:
            try:
                username = input("Enter your username:")
                    if username not in [user_database]:
                        print ("User not found. Try again")
                        continue

                    if username in [user_database]:
                        continue

                    password = input("Enter your password:")
                        if password not in [user_database]:
                            print ("Password incorrect. Try again")
                            continue

                        if password in [user_database]:
                            continue
            except ValueError as e:
                print(e)
                    
            