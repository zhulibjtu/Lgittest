import os  # Import the OS module

MESSAGE = 'The directory already exists.'
TESTDIR = 'testdir'



try:
    home = os.path.expanduser("~")  # Set the variable home by expanding the user's set home directory
    print(home)  # Print the location

    if not os.path.exists(os.path.join(home, TESTDIR)):  # os.path.join() for making a full path safely
        os.makedirs(os.path.join(home, TESTDIR))  # If not create the directory, inside their home directory
    else:
        print(MESSAGE)
except Exception as e:
    print(e)

items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
print(items1)


items2 = [x ** 2 for x in range(1, 10) if x % 2]
print(items2)