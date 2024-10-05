# Title: LabX Mobile
#### Video Demo:  [youtube video](https://youtu.be/NY7KezwHg6w?si=U563QnuecfbeZ9Vq)
#### Description: Python project aiming to handle user interaction for a shop system where users can log in, sign up, and navigate through various product categories like mobiles and laptops. The UI uses keyboard inputs for navigation(up, down, enter, tab), and the shopping experience includes adding items to a cart, viewing them, drop items from cart,and checking out.

## Libraries
- **termcolor**: used from this module *colored* function to color text *colored(str, color)*
- **tabulate**: used from this module *tabulate* to make table for data
- **pyfiglet**: used from this module *figlet_format* to make shape for name pages

>**To install libraries**

```pip install -r requirements.txt```

## How to work this project after run program
1- Choose login or sign up by keyboard (up, down) and use (enter) from keyboard to call this page

2- Fill in the information according to the conditions to enter the program

3- When ending from login or sign up choose section from mobiles or laptops by same way of step 1

4- Choose company

5- Will appear table of models of devices with price for every model

6- Enter name of model to add it to cart

> [!NOTE]
> After enter name of model, If you press **tab** will open page of cart else write name of another model

7- When open cart user can continue buy things by **tab**, can buy this items by **enter**, can drop items by **-**

## project.py
### First section (login, sign up)

#### main function
> *main()* used to login or sign up by keyboard through function **event_keyboard()** and call function **shape(choice, arrow)** to draw shape like rectangle around word

> keyboard keys used in this page:

    - enter: For choose
    - tab: terminate program
    - up: move up
    - down: move down

#### shape function
> *shape(choice, arrow)* used to draw shape like rectangle around word and make arrow next to the word that user move to it

#### login function
- Ask user for username
  - check username exist in file before or not
    - if username does not exist ask user for press on *y* for sign up or any key to enter username again

- Ask user for password
  - check password match with username or not by **check_password(name, password)**
    - if password not match ask user for press *y* for enter new password via **forget_password()** or any key to enter password again
        - *forget_password()* ask user for gmail account to send otp  for enter new password and confirm it

- Enter to *shop_fn()* after


#### sign up function
- Ask user for username
  - check username exist in file before or not by **check_username(name)**
    - if username exist ask user for enter another username
    - check format of username by regular expression **format_username(name)**
    - username save in class attribute called name from class *User*

- Ask user for email
   - check email exist in file before or not by **check_email(email)**
    - if email exist do same thing that happen in username
    - check format of email by regular expression **format_email(email)**
    - email save in class attribute called email from class *User*

- Ask user for password
  - enter to *enter_password()* function for enter password under certain conditions
    - check format of password by regular expression **format_password(password)**
  - enter to *confirm password(password, flag=False)* function for enter same password again
  - save name, email, password in csv file

- Enter to *shop_fn()*

#### format_username function
>**format_username(name)** used to match pattern of name with maked pattern before by regular expression of *re* library

#### format_email function
>**format_email(email)** used to match pattern of email with maked pattern before by regular expression of *re* library

#### format_password function
>**format_password(password)** used to match pattern of password with maked pattern before by regular expression of *re* library

#### check_username function
> **check_username(name)** used to check if username in file or not

#### check_email function
> **check_email(email)** used to check if email in file or not

#### check_passsword function
> **check_password(name, password)** used to check if password match username from file

#### enter_password function
> **enter_password()** when call it ask user to enter password according to the conditions

#### confirm_password function
> **confirm_password(password, flag=False)** when call it

    - ask user for enter password again to match it with what user entered before
        - if user enter it incorrect will ask user for enter password again press y or enter confirm again

#### forget_password function
> **forget_password()** call it for update password

    - Ask user for enter email that match with username to send otp via OTP(email)
    - After send otp, ask user for enter otp
        - If otp correct user will enter new password via enter_password() and confirm it via confirm_password(password, flag=True)
        - Else user can write it again or want to send another one

#### get_email function
> **get_email()** to get email after do login and save it in *email* attribute from calss *User*

#### save_data function
> **save_data()** Save useranme, email, password in file according to fieldnames

#### update_password function
> **update_password(email, new_password)** update password in file after search about email in file


#### clear_terminal function
> **clear_terminal()** used to clear terminal like going to new page
with choice if platform Windows , Mac, Linux

#### Detect char will pressed and return it
#### getch function
> **getch()** read single character from input and not write it on terminal

#### get_key_name function
> **get_key_name(char)** used to return name of button that pressed

#### event_keyboard function
> **event_keyboard()** used to listen by **getch()** and return name of key by **get_key_name(char)**


### Second section
#### shop_fn function
> *shop_fn()* function used to choose mobiles or laptops by keyboard through function **event_keyboard()**

> keyboard keys:

    - enter: For choose
    - tab: to logout
    - up: move up
    - down: move down

#### choose function
> **choose(choice, arrow)** to put arrow to next the word that user move to it

#### mobiles function
> *mobiles()* function used to choose mobile company by keyboard through function **event_keyboard()**

> keyboard keys:

    - enter: For choose
    - tab: return to shop_fn()
    - up: move up
    - down: move down

#### apple_mob() function
> *apple_mob()* show table of apple mobiles from dictionary called apple_mobiles after that user enter model to buy by **model_for_buy(<name_of_model>)** talk about it later

#### samsung_mob() function same thing of apple_mob()
#### oppo_mob() function same thing of apple_mob()


#### labs function
> *labs()* function used to choose laptop company by keyboard through function **event_keyboard()**

> keyboard keys:

    - enter: For choose
    - tab: return to shop_fn()
    - up: move up
    - down: move down

#### apple_lap() function
> *apple_lap()* show table of apple laps. from dictionary called apple_laptops after that user enter model to buy by **model_for_buy(<name_of_model>)** talk about it later

#### hp_lab() function same thing of apple_lap()
#### dell_lap() function same thing of apple_lap()


#### model_for_buy function
> *model_for_buy(type_of_devices)* take a dictionary as argument
- Show the models and prices in table from *tabulate* module by function **show_table(type)**
- Ask user for enter name of model **search_model(model, models)** and go to **cart()** function
    - If exist in this table will add to cart **add_to_cart(model, price)**
    - Else program tell user that model does not exist and ask him for enter another model or go previous page by (tab) word or keyboard key

#### add_to_cart function
> **add_to_cart(model, price)** add price of model to total price and append [model, price] to list called *cart_items*

#### cart function
> *cart()* will show to user table of all items that added to cart with choice for continue buy devices(tab), verify buy(enter), drop items from cart(-)

#### bought_items function
> *bought_items()* will send message on gmail **OTP(email, message = cart_items)** message of total price and back to **shop_fn()**

#### drop_items function
> *drop_items()* will show table of cart
- Ask user for enter model to drop it from table or "tab" to go to cart
- If user enter name of model will check if model exist in cart or not
    - If model exist will remove price from total price, remove model from *cart_items*list and row of model from table

#### way_to_back function
> ***way_to_back()*** used to determine any page will return to it

#### shape_font function
> **shape_font(text, font)** used to write name of pages in specific font

#### show_table function
> **show_table(type, flag=True)** if argument dictionary will convert it to list of list via **convert_to_list_of_list(type)** and show it as table, else (cart is list of list) will show directly


## content_data.py
> This page has dictionaries for mobiles and laptops comapny models

#### convert_to_list_of_list function
> **convert_to_list_of_list(dict_)** Convert dictionary to sorted list of list based on price first and name after that


## otp.py
### OTP function
> **OTP(email, message="otp")** used to send email to user for verification code or total price

### verify_otp function
> **verify_otp(received_otp, generated_otp)** verify received otp from user with generated

## test_project.py
> Has functions to test functions from *project.py* and *content_data.py*
- **test_format_username()**
- **test_format_email()**
- **test_format_password()**
- **test_search_model()**
- **test_convert_to_list_of_list()**

## user.py
> Inside it *User* calss has attributes and it setter and getter functions
- *username*
- *email*
- *password*
