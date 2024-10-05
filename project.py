import csv
import os
import pyfiglet
import re
import sys
import termios
import time
import tty
from tabulate import tabulate
from termcolor import colored
from user import User
from otp import OTP, verify_otp
from content_data import samsung_mobiles, apple_mobiles, oppo_mobiles,\
                         dell_laptops, apple_laptops, hp_laptops, convert_to_list_of_list


total_price = 0
cart_items = []
page = None



def main():
    choice = {
        "Login":8,
        "Sign up": 10
    }

    i = 1
    shape(choice, 1)
    while(True):
        char = event_keyboard()

        match char:
            case "down":
                if i != 1:
                    i -= 1
                    shape(choice, i)
                else:
                    i = 2
                    shape(choice, i)


            case "up":
                if i != 2:
                    i += 1
                    shape(choice, i)
                else:
                    i = 1
                    shape(choice, i)

            case "enter":
                if i == 1:
                    login()
                else:
                    sign_up()

            case "tab":
                sys.exit()


def shape(choice, arrow):
    clear_terminal()
    print(colored(shape_font(f"{'':25}LabX Mobile", "big"), "cyan"))
    for i, key in enumerate(choice):
        width = choice[key]
        print(f"{'':10}", end="")
        # to make first line ╔════════╗
        for w in range(width):
            if w == 0:
                print("╔", end="")

            print("═", end="")

            if w == width - 1:
                print("╗", end="")
        print()



        if arrow == i + 1:
            print(colored(f"{'-->':9}", "green"), "║",end="")
        else:
            print(f"{'':9}", "║",end="")

        if width == 8:
            print("", colored(f"{key:7}", "red"), end="")
            print("║")
        else:
            print("", colored(f"{key:9}", "red"), end="")
            print("║")


        for w in range(width):
            if w == 0:
                print(f"{'':9}","╚", end="")

            print("═", end="")

            if w == width - 1:
                print("╝", end="")
        print()

    return

# Login Page
def login():
    clear_terminal()
    print(colored(shape_font(f"{'':60}Login", "mini"), "grey"))
    while True:
        name = input("Enter username: ").strip()

        if not check_username(name):
            print(colored("Username does not exist😔\nIf you need sign up press y, or any key to continue", "red"))
            # time.sleep(2)
            char = event_keyboard()
            if char in ["y", "Y"]:
                sign_up()
        else:
            User.username = name
            break

    while True:
        password = input("Enter password: ")
        if not check_password(name, password):
            print(colored("Password is wrong😯\nIf you forget password enter y, or any key to continue", "red"))
            # time.sleep(2)
            char = event_keyboard()
            if char in ["y", "Y"]:
                forget_password()
                break
        else:
            User.password = password
            get_email()
            break

    shop_fn()
    return

# Sign up Page
def sign_up():
    clear_terminal()
    print(colored(shape_font(f"{'':60}Sign up", "mini"), "grey"))
    # For enter username
    while True:
        print(colored("Username characters, digits, _", "green"))
        name = input("Enter username: ").strip()
        # Check for true format
        if format_username(name):
            # Check if username exist before
            if check_username(name):
                print(colored("Username Exists Before❗", "red"))
            else:
                User.username = name
                break
        else:
            print(colored("Username format not true❗", "red"))

    print()
    # For enter email
    while True:
        print(colored("Email must end with @gmail.com", "green"))
        email = input("Enter email: ").strip()
        # Check for true format
        if format_email(email):
             # Check if email exist before
            if check_email(email):
                print(colored("email Exists Before❗", "red"))
            else:
                User.email = email
                break
        else:
            print(colored("Email format not true❗", "red"))

    print()
    # For enter password
    while True:
        password = enter_password()
        confirm_password(password)
        # Enter username , password, email to file
        save_data()
        # Enter to program
        shop_fn()
        break

    return

# Check username format
def format_username(name):
    return True if re.search(r"^\w+$", name) else False

# Check email format
def format_email(email):
    return True if re.search(r"^.+[\w\S.%+-]+@gmail\.com$", email, re.IGNORECASE) else False

# Check password format
def format_password(password):
    return True if re.search(r"^(?=.*[\d])(?=.*[*!@#$%^&*.,])[\w*!@#$%^&*.,]{8,}$", password) else False

# Check username exist in file or not
def check_username(name):
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if name == row["name"]:
                return True
    return False

# Check email exist in file or not
def check_email(email):
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if email == row["email"]:
                return True
    return False

# Check password match username or not
def check_password(name, password):
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if name == row["name"]:
                if password == row["password"]:
                    return True
    return False

# For enter password
def enter_password():
    verify_pass = ["consists at least 8 characters", "including at least one of * ! @ # % , . $ & ", "including at least one digit"]

    print()
    for i, condition in enumerate(verify_pass, start=1):
            print(colored(f"{i}- {condition}", "green"))
    print()
    while True:
        password = input("Enter password: ")
        if format_password(password):
            break
        else:
            print(colored("Password not accroding to conditios❗", "red"))

    return password

# Check for confirm password same with password
def confirm_password(password, flag=False):
    while True:
        if flag:
            confirm_pass = input("Enter confirm new password: ")
        else:
            confirm_pass = input("Enter confirm password: ")

        if password != confirm_pass:
                print(colored("Confirm password NOT match password❗\nIf you need to enter password again press y, or any key to continue", "red"))
                # time.sleep(2)
                char = event_keyboard()
                if char in ["y", "Y"]:
                    password = enter_password()
                    confirm_pass = None
        else:
            break

    User.password = confirm_pass

# Enter new password
def forget_password():
    clear_terminal()
    print(colored(shape_font(f"{'':30}Forget Password", "mini"), "red"))
    flag = False
    while True:
        email = input("Enter your email to send OTP: ")
        # Check if name match with email
        with open("data.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if User.username == row["name"] and email == row["email"]:
                    flag = True
                    break

            if flag:
                break
            else:
                print(colored("Email does not exist❗", "red"))



    spinner = ['|', '/', '-', '\\']
    for i in range(15):
        sys.stdout.write('\rwait for send otp ' + spinner[i % len(spinner)])  # Print the spinner character
        sys.stdout.flush()
        time.sleep(0.1)

    generated_otp = OTP(email)

    while True:
        recieve_otp = input(colored("\nEnter sent OTP: ", "green")).strip()
        if verify_otp(recieve_otp, generated_otp):
            new_password = enter_password()
            confirm_password(new_password, flag=True)
            update_password(email, User.password)
            break

        else:
            print(colored("OTP not true press y to resend❗ or any key to continue", "red"))
            # time.sleep(2)
            char = event_keyboard()
            if char in ["y", "Y"]:
                generated_otp = OTP(email)

# Get email from file
def get_email():
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if User.username == row["name"]:
                User.email = row["email"]

# Write data in file
def save_data():
    with open("data.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "password", "email"])
        writer.writerow({"name":User.username,
                         "password":User.password,
                         "email":User.email})

#For update password
def update_password(email, new_password):
    # Read data from csv file
    rows = []
    with open("data.csv", 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["email"] == email:
                row["password"] = new_password  # Update the password
            rows.append(row)

    # Write the updated data back to the CSV file
    with open("data.csv", 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "password", "email"])
        writer.writeheader()  # Write the header
        writer.writerows(rows)  # Write the updated rows

# Clear terminal
def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def get_key_name(char):
    special_keys = {
        '\x1b': 'esc',
        '\x7f': 'backspace',
        '\r': 'enter',
        ' ': 'space',
        '\t': 'tab',
        '\x1b[A': 'up',
        '\x1b[B': 'down',
        '\x1b[C': 'right',
        '\x1b[D': 'left'
    }
    if char in special_keys:
        return special_keys[char]
    elif len(char) == 1 and ord(char) < 32:
        return f'ctrl+{chr(ord(char) + 64).lower()}'
    else:
        return char

# For listen press on any key from keyboard
def event_keyboard():
    char = getch()
    if char == '\x1b':
        next_char = getch()
        if next_char == '[':
            last_char = getch()
            char += next_char + last_char

    key_name = get_key_name(char)
    return key_name

# Shop function
def shop_fn():
    choice = ["Mobiles", "Laptops"]
    i = 1
    choose(choice, i, "LabX Mobile")
    while(True):
        char = event_keyboard()

        match char:
            case "down":
                if i != 1:
                    i -= 1
                    choose(choice, i, "LabX Mobile")
                else:
                    i = 2
                    choose(choice, i, "LabX Mobile")

            case "up":
                if i != 2:
                    i += 1
                    choose(choice, i, "LabX Mobile")
                else:
                    i = 1
                    choose(choice, i, "LabX Mobile")

            case "enter":
               mobiles() if i == 1 else labs()

            case "tab":
                global cart_items, total_price
                cart_items = []
                total_price = 0
                main()
                break
    return


def choose(choice, arrow, word):
    clear_terminal()
    print(shape_font(f"{'':40}{word}", "mini"))
    for i, key in enumerate(choice):
        if arrow == i + 1:
                print(colored(f"{'-->':5} {key}", "green"))
        else:
            print(f"{'':5} {key}")
    return

# Mobile page for chooce
def mobiles():
    choice = ["Apple" , "Samsung", "Oppo"]
    i = 1
    choose(choice, i, "Mobiles Page 📱")
    while(True):
        char = event_keyboard()
        match char:
            case "down":
                if i == 3:
                    i = 1
                    choose(choice, i, "Mobiles Page")
                else:
                    i += 1
                    choose(choice, i, "Mobiles Page")

            case "up":
                if i == 1:
                    i = 3
                    choose(choice, i, "Mobiles Page")
                else:
                    i -= 1
                    choose(choice, i, "Mobiles Page")

            case "enter":
                if i == 1:
                    apple_mob()
                elif i == 2:
                    samsung_mob()
                else:
                    oppo_mob()

            case "tab":
                shop_fn()
                break

# Apple mobiles
def apple_mob():
    clear_terminal()
    print(shape_font(f"{'':30} Apple Mobiles", "mini"))
    print
    global page
    page = "m"
    model_for_buy(apple_mobiles)

# Samsung mobiles
def samsung_mob():
    clear_terminal()
    print(shape_font(f"{'':30}Samsung Mobiles", "mini"))
    global page
    page = "m"
    model_for_buy(samsung_mobiles)

# Oppo mobiles
def oppo_mob():
    clear_terminal()
    print(shape_font(f"{'':30}Oppo Mobiles", "mini"))
    global page
    page = "m"
    model_for_buy(oppo_mobiles)

# Labs page for choose
def labs():
    choice = ["Apple", "HP", "Dell"]

    i = 1
    choose(choice, i, "Laptops Page 💻")
    while(True):
        char = event_keyboard()

        match char:
            case "down":
                if i != 3:
                    i += 1
                    choose(choice, i, "Laptops Page")
                else:
                    i = 1
                    choose(choice, i, "Laptops Page")

            case "up":
                if i != 1:
                    i -= 1
                    choose(choice, i, "Laptops Page")
                else:
                    i = 3
                    choose(choice, i, "Laptops Page")

            case "enter":
                if i == 1:
                    apple_lap()
                elif i == 2:
                    hp_lap()
                else:
                    dell_lap()

            case "tab":
                shop_fn()
                break

# Apple Laps.
def apple_lap():
    clear_terminal()
    print(shape_font(f"{'':30}Apple Laptops", "mini"))
    global page
    page = "l"
    model_for_buy(apple_laptops)

# HP Laps.
def hp_lap():
    clear_terminal()
    print(shape_font(f"{'':30}HP Laptops", "mini"))
    global page
    page = "l"
    model_for_buy(hp_laptops)

# Dell Laps.
def dell_lap():
    clear_terminal()
    print(shape_font(f"{'':30}Dell Laptops", "mini"))
    global page
    page = "l"
    model_for_buy(dell_laptops)

# Function for make search of devices and add to cart
def model_for_buy(type_of_devices):
    print(colored("Note: ", "green") + "Any model in table exist in shop")
    print(show_table(type_of_devices))

    while True:
        search = input("Enter model to add to cart (press tab to end or write it): ").strip()
        if search.lower() == "tab":
            cart()
            break
        if not search_model(search.strip(), type_of_devices):
            print(colored("Model does not exist in shop, sure from model name", "red"))



        # time.sleep(0.5)
        if event_keyboard() == "tab":
            if cart_items:
                cart()
                break
            else:
                shop_fn()

# search in dict. for device
def search_model(model, models):
    for key in models.keys():
        if model.strip().lower() == key.lower():
            add_to_cart(key, models[key])
            return True
    return False

# Add device to cart
def add_to_cart(model, price):
    global total_price, cart_items
    total_price += int(price)
    cart_items.append([model, price])

# Cart Page
def cart():
    clear_terminal()
    print(shape_font(f"{'':50}Cart🛒", "mini"))
    global cart_items, total_price
    edit_cart = []
    for item in cart_items:
        if item[0] != "Total":
            edit_cart.append(item)
    cart_items = edit_cart
    cart_items.append(["Total", total_price])
    print(show_table(cart_items, False))
    print("Press enter to buy items " + colored("\n If you need to drop any item press (-)", "green") +\
          colored("\n  If you need to continue press (tab)", "green"))

    while True:
        match event_keyboard():
            case "enter":
                bought_items()

            case "tab":
                way_to_back()

            case "-":
                drop_items()

# After verificate buy
def bought_items():
    global cart_items
    if total_price == 0:
        return
    clear_terminal()
    print(shape_font("Thank you for using LabX Mobile", "mini"))
    print(colored(shape_font("Check your gmail", "bubble"), "green"))
    OTP(User.email, message=cart_items)
    time.sleep(2)
    cart_items = []
    shop_fn()

# Drop items from cart
def drop_items():
    global total_price, cart_items
    clear_terminal()
    print(shape_font(f"{'':50}Drop items", "mini"))

    print(show_table(cart_items, False))
    while True:
        drop_item = input("Enter name of model to drop it (press tab or write it to end): ").strip().lower()

        if drop_item.lower() == "total":
            flag = False
        else:
            flag = True

        if drop_item.lower() == "tab":
            cart()


        index = None
        for i , item in enumerate(cart_items):
            if item[0].lower() == drop_item:
                index = i
                break

        if index != None and flag:
            total_price -= cart_items[index][1]
            cart_items_edit = []
            for i in range(len(cart_items)):
                if i != index:
                    cart_items_edit.append(cart_items[i])

            cart_items = cart_items_edit

            # time.sleep(0.2)
            if event_keyboard() == "tab":
                cart()
                break
        else:
            print(colored("Not found this item in cart", "red"))


def way_to_back():
    global page
    match page:
        case "m":
            mobiles()
        case "l":
            labs()
        case _:
            shop_fn()


def shape_font(text, font):
    return pyfiglet.figlet_format(f"{text:6}", font=font)

# Make table
def show_table(type, flag = True):
    headers = list(["Model", "Price $"])
    headers = [colored(headers[0], "red"), colored(headers[1], "green")]
    headers = [str(headers[0]).center(25), str(headers[1]).center(20)]

    if flag:
        rows = convert_to_list_of_list(type)
    else:
        rows = type

    rows = [color_rows(row) for row in rows]
    rows = [center_rows(row) for row in rows]

    # Create table
    data = tabulate(rows, headers=headers, tablefmt="fancy_grid")

    # Display the table
    return data


def color_rows(row):
    return [colored(row[0], "red"), colored(str(row[1]), "green")]


def center_rows(row):
     return [str(row[0]).center(50), str(row[1]).center(20)]


if __name__ == "__main__":
    main()
