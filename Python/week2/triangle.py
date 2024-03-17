n = int(input("Input n: "))

with open('star.txt', 'w') as file :
    for i in range(n) :
        for j in range(i+1) :
            file.write("*")
        file.write("\n")