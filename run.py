
import pyperclip
from user import User
from user import Credentials

/usr/bin/env python3.6

def create_user(firstname,lastname,username,userpassword):
    newuser= User(firstname,lastname,username,userpassword)
    return newuser

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()
def find_user(number):
    return User.find_by_number(number)
def display_users():
    return User.display_users()

def create_account(accountusername,accountname,accountpassword):
    newaccount=Credentials(accountusername,accountname,accountpassword)
    return newaccount
def save_account(user):
    user.save_account()
def delete_account()
def find_account(number):
    return Credentials.find_by_number(number)
def display_accounts():
    return Credentials.display_accounts()


def main():
        while True:
            print("welcome to password Vault write SU or LG to start")
            print("SU -or- LG")
            option=input()
            if option == "SU":
                print("create Account")
                print("-"*10)   
                print("enter your first name..")  
                firstname=input()
                print("enter your last name..")
                lastname=input()
                print("set your username..")
                username=input()
                print("set your password..")
                userpassword=input()


if __name__ == '__main__':
    main()












