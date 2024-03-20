def main() :
    birthYear = int(input("Input your birth year: "))
    age = 2024 - birthYear + 1
    if age > 26 :
        print("TteulDdak")
    elif age >= 20 :
        print("Undergraduate student")
    elif age >= 17 :
        print("High school student")
    elif age >= 14 :
        print("Middle school student")
    elif age >= 8 :
        print("Elementary school student")
    else :
        print("Jammin")
        
if __name__ == '__main__' :
    main()