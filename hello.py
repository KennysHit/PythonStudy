if __name__ == '__main__':
    print("Hello World!")

    name = input("what is your name?")
    birth_year = input("what is your birth_year?")
    age = 2019 - int(birth_year)
    print(type(birth_year))
    print("name is : " + name + " , age is : " + str(age))

    talk = """
    **********************
    Hi Tom,
        It's gland to see you!
        How do you do?
    **********************
    """
    print(talk)

    testStr = "this is a string"
    print(testStr[-2])
    print(testStr[1:])
    print(type(testStr[0]))

    firstName = "Tom"
    lastName = "Simith"
    message = f"{firstName} [{lastName}] is a coder"
    print(message)
    print(len(message))
    print("Tom" in message)

    weather = "bad"
    if weather == "good":
        print("It's a good day")
        print("Enjoy your day")
    elif weather == "bad":
        print("It's a bad day")
        print("Try to relax yourself")
    else:
        print("End!")

    try:
        weight = int(input("Input your weight:"))
        unit = input("Choose your input unit of (L)bs or (K)g:")
        if unit.upper() == "L":
            print(f"Your weight is {weight * 0.45} Kilos")
        elif unit.upper() == "K":
            print(f"Your weight is {weight / 0.45} pounds")
        else:
            print("Unit input error!")
    except ValueError:
        print("The weight should be a integer!")

    choose = input("> ").lower()
    is_carStart = False
    helper = """
    start --- To start the car!
    stop --- To stop the car !
    quit --- To quit this program!
    """
    while choose != "quit":
        if "start" == choose:
            if not is_carStart:
                print("Car started!")
                is_carStart = True
            elif is_carStart:
                print("The car has already started!")
        elif "stop" == choose:
            if is_carStart:
                print("Car stopped!")
                is_carStart = False
            elif not is_carStart:
                print("The car hasn't started!")
        elif "help" == choose:
            print(helper)
        else:
            print("I can't understand your meaning , you can input 'help' for help")
        choose = input("> ").lower()
    else:
        print("End!")

    number = [5, 2, 5, 2, 2]
    for x in number:
        str0 = ""
        for y in range(x):
            str0 += "*"
        print(str0)

    num = [2, 4, 1, 6, 8, 6, 9, 11, 3, 4]
    maxi = num[0]
    for x in num:
        if maxi < x:
            maxi = x
    print(maxi)

    num = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for row in num:
        for spa in row:
            print(spa)


    def emote_transform(message):
        emote = {
            ":)": "😀",
            ":(": "😕"
        }
        words = message.split(" ")
        str1 = ""
        for word in words:
            str1 += emote.get(word, word) + " "
        return str1


    print(emote_transform(input(">")))


    class Person:

        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

        def say_hello(self):
            print(f"Hi , I am {self.first_name} {self.last_name}")


    class Student(Person):
        pass

        def __init__(self, first_name, last_name, school):
            self.first_name = first_name
            self.last_name = last_name
            self.school = school

        def self_introduction(self):
            print(f"I study in {self.school}")


    student1 = Student(first_name="Li", last_name="Xiaoping", school="Sichuan University")
    student1.say_hello()
    student1.self_introduction()

