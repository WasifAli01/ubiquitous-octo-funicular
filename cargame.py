# Ask The User's Name
user_name = input("Hey there! What should I call you?")
# welcome the user with his/her name.
print(f"Hello {user_name}! Welcome To Car Game!")
# Start getting commands from user
# Set a variable with an empty string
command = ''
# Set two booleans for car's position i.e. is it started or stopped?
is_started = False  # As We Know Car Is Currently stopped.
is_stopped = True  # Because It is stopped.
# If You dont know what are True or False. So in programming these are called "Boolean Variables." They can be only either True or False.
while command != 'quit':
    # != means not equal to in python
    command = input('>>> ').lower()
    # You may be wondering why I used lower() method. It is because whenever user gives input either in lower case letters or uppercase letters it will accept both.
    # Here We Are Using while loop because we do not knwo after how many times the user will enter 'quit' as command and for how many numbers of time our statment will be repeated.
    # So while command is not equal to quit the program will keep asking for command input.
    # Now we will tell programs to make decision for correct statments. Using if, elif(short for elseif) and else statements.
    # So:
    if command == 'start':
        if not is_started:
            is_started = True
            is_stopped = False
            print("Car Started. Let's Go!")
            # So what is going on here? We are telling the python that if the car is not started then set our is_started variable to True and is_stopped variable to False and simply print on console that car is started.
        elif is_started:
            print(f'Hey {user_name}! Car Is Already Started. You are a Noob.')
            # Other wise else if our is started variable is already True, means our car is already started so our program will bully the user.
    elif command == 'stop':
        if not is_stopped:
            is_stopped = True
            is_started = False
            print('Car Is Stopped!')
        elif is_stopped:
            print(f'Hey {user_name}! Car Is Already Stopped!. You are a Noob.')
    # Now I want you to uenderstand this piece of code by yourself. It is completely same as the upper one. Just using different variable for decision making and printing something else but logic is same.
    elif command == 'help':
        print('''
I am here for Your Help.
Following the commands are supported.
1.  start - To Start The Car
2.  stop - To Stop The Car
3.  quit - To Quit The Game
''')
# You may Now wonder why are we using 3 quotation marks? Well it is because we are printing multiple lines on terminal. Instead of writing print statement 3 times you can just simply use 3 quotation marks to print multiple lines.
    # Now Time To Tell This Program when it should stop. It's Simple
    elif command == 'quit':
        break
    # So Whenever The user gives quit command the program terminates.
# Hope You May Understand it till here. Now we will use else statement because no other command is left.
# So:
    else:  # If the user's given command is not from one of the available commands, it will print following line.
        print(
            f"Hey {user_name} I can't understand this command. Kindly type help to see available commands. :)")


# So this was a basic example of how the cores of programs works. Hope it clears your mind.
