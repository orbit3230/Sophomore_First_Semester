import random

def generate_number() :
    answer = []
    for i in range(3) :
        next = random.randrange(1, 10)
        print(next)
        print(i)
        if(next in answer) :
            i -= 1
            continue
        else :
            answer.append(next)
    return answer
    
def check(guess, answer) :
    strike = 0
    ball = 0
    for i in range(len(guess)) :
        if(guess[i] in answer) :
            if(guess[i] == answer[i]) :
                strike += 1
            else :
                ball += 1
    return strike, ball

def input_guess_number() :
    answer = []
    answer.append(int(input("Input 0st number: ")))
    answer.append(int(input("Input 1st number: ")))
    answer.append(int(input("Input 2st number: ")))
    return answer
    
def main() :
    answer = generate_number()
    print(answer)
    while(True) :
        guess = input_guess_number()
        strike, ball = check(guess, answer)
        if(strike == 3) :
            print("Correct!! answer numbers: " + str(answer))
            break
        else :
            print("Wrong (hint: %d strike, %d ball)" % (strike, ball)) 
    
if __name__ == '__main__' :
    main()