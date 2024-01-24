import sqlite3
import sys
import random

def main():
    makedb()
    if izberi_pot():
        print("")
        print("You are online!")
        rockpaperscissors()
    else:
        main()


def izberi_pot():
    print("1/2")
    choice = input("Log in/Sign up:")
    if choice.lower() == "1":
        if log_in():
            return True
    elif choice.lower() == "2":
        create_password()
        if log_in():
            return True
        else:
            main()


def makedb():
    con = sqlite3.connect("novikurac5.db")
    con.execute("CREATE TABLE IF NOT EXISTS accounts(name TEXT, password TEXT)")


def create_password():
    try:
        cn1 = sqlite3.connect("novikurac5.db")
        cursor = cn1.cursor()
        cursor.execute(f"SELECT name FROM accounts")
        name1 = input("Create a name:")
        list = ()
        for name in cursor:
            list += name
        while len(name1) < 2:
            name1 = input("Enter a name that has 2 letters:")
        while name1 in list:
            print("Name is already taken! Chose another one!")
            name1 = input("Create a name:")
        password = input("Create a password:")
        c = any(x.isdigit() for x in password)
        while len(password) < 6 or bool(c) != True:
            password = input("Use a password with 6 characters and numbers:")
            c = any(x.isdigit() for x in password)
        checkpass = input("Re-enter your password:")
        while checkpass != password:
            print("Password don't match!")
            checkpass = input("Re-enter your password:")
        print("Account created!")

        con = sqlite3.connect("novikurac5.db")
        con.execute(f"INSERT INTO accounts(name, password) VALUES('{name1}','{password}')")
        con.commit()
        con.close()
    except:
        return True


def log_in():
    c_name = input("Enter a name to log in:")
    cn1 = sqlite3.connect("novikurac5.db")
    cursor = cn1.cursor()
    cursor.execute(f"SELECT name, password FROM accounts WHERE name = '{c_name}'")
    try:
        c = []
        p_password = input("Enter a password to log in:")
        for name, password in cursor:
            c.append(password)
        while p_password != c[0]:
            print("Password incorrect, try again!")
            p_password = input("Enter a password to log in")
        print("Log In Successful!")
        return True
    except:
        print(f"{c_name} not exists")
        return False


def rockpaperscissors():
    your_score = 0
    ai_score = 0
    while your_score < 3 and ai_score < 3:
        izbira = {"kamen": "🪨", "skarje": "✂️", "list": "🧻"}
        moznosti = list(izbira.keys())
        ai = random.choice(moznosti)
        you = ""
        while you not in moznosti:
            you = input("Enter kamen/skarje/list:")
        print(f"You: {izbira[you]}")
        print(f"AI: {izbira[ai]}")

        if you == ai:
            print("It's a tie!")
        elif you == "kamen" and ai == "skarje":
            print("You win")
            your_score += 1
        elif you == "skarje" and ai == "list":
            print("You win")
            your_score += 1
        elif you == "list" and ai == "kamen":
            print("You win")
            your_score += 1
        else:
            print("AI win!")
            ai_score += 1
        print(f"YOU: {your_score}")
        print(f"AI: {ai_score}")
    print("*" * 30)
    if your_score == 3:
        print(f"WINNER!\nYOU: {your_score}\nAI: {ai_score}")
    else:
        print(f"LOSER...\nAI: {ai_score}\nYOU: {your_score}")

def izpisi_db():
    cn1 = sqlite3.connect("novikurac5.db")
    cursor = cn1.cursor()
    cursor.execute(f"SELECT name, password FROM accounts")

    for name, password in cursor:
        print(f"name:{name}    password:{password}")


izpisi_db()
main()



