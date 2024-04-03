def main() :
    f = open(r".\yesterday.txt", "r", encoding="utf-8")
    
    lyrics = f.readlines()
    f.close()
    
    count = 0
    
    for line in lyrics :
        if 'yesterday' in line.lower() :
            count += 1
            
    print(f"Number of a word \'yesterday\': {count}")
    
if __name__ == "__main__" :
    main()