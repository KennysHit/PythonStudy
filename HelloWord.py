import time

if __name__ == '__main__':
    hello = """
***************************
    hello word !
    welcome to Python~
***************************
    """
    print(hello)

    name = input("Please input your name: ")
    birthday = input("Please input your birthday: ")

    age = int(time.strftime("%Y", time.localtime(time.time()))) - int(birthday)

    if age < 18:
        name = name + " boy"
    elif age >= 18:
        name = "Mr." + name

    print(f"\nhey {name}, wish you have a good trip in Python!")

