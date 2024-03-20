import random

def main() :
    answer = random.randint(1, 10)
    while(True) :
        guess = int(input("Input any number(1 - 10): "))
        if(guess is answer) :
            print("Correct answer! The right answer is %d" % guess)
            break
        if(guess > answer) :
            print("Guess smaller number")
        else :
            print("Guess bigger number")
            
if __name__ == '__main__' :
    main()