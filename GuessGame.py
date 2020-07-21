import random
import time


def is_inputLegal(num):
    if 1 <= num <= 100:
        return True
    else:
        raise ValueError


if __name__ == '__main__':
    sec = random.randint(1, 100)  # 生成1-100之间一个随机的整数
    print("""
    *******************************************************************
        There is a number between 1 and 100, let's try to guess it!
    *******************************************************************    
    """)
    while True:
        try:
            guess = int(input("Please input your guess number: "))
            is_inputLegal(guess)
            while sec != guess:
                if sec > guess:
                    print("Your guess is a little small～")
                    guess = int(input("Please input your guess number again: "))
                    is_inputLegal(guess)
                elif sec < guess:
                    print("Your guess is a little high～")
                    guess = int(input("Please input your guess number again: "))
                    is_inputLegal(guess)

            print(f"\n\nRight it's {sec}, you guessed the right number！Congratulations, you win!!!!")
            break
        except ValueError:
            print("Input error: The guess number should be a integer and between 1 and 100!")
            time.sleep(1)
