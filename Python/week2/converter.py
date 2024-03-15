def main() :
    print("This program converts Celsius to Farenheit")
    c = float(input('Current Celsius: '))
    f = (c*1.8) + 32
    print(f'Celsius = {c}')
    print("Farenheit: {:.2f}".format(f))
    
if __name__ == '__main__' :
    main()