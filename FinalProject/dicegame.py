from datetime import datetime
import random


def main():
    print ("Welcome to Dice Roll game!")
    print ("1. Register")
    print ("2. Log in")
    print ("3. Exit")
    
    choice = int(input("Enter  your choice: "))
    if choice == '1':
        (lagay mo dito yung filename).User_manager.register():



class Dice_game:
    def play_game():
        cpu_dice_number = random.randint(1,6)

        print("CPU Dice number is: {cpu_dice_number}")

        user_dice_number = random.randint(1,6)

        print(" Dice number is: {cpu_dice_number}")

    def save_scores():
        pass
    def show_top_scores():
        pass

 




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
            




                
        