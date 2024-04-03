def processing(line) :
    max_index = len(line)
    lines = []
    next_character = ''
    character_index = 0
    # 우선 모든 문자들을 대문자로 변환(alphabetical 한 문자만을 대상으로)
    for character in line :
        if character.isalpha() :
            charater = chr(ord(character) + 32)
    while True :
        # 만약 '.'을 만나면 다음 단어부터는 다음 줄(배열 인덱스)에 저장
        next_character = line[character_index]
        character_index += 1
        if next_character == '.' :
            # 처음부터 `.`이 처음 나타난 곳 까지를 한 문장으로 배열에 저장
            lines.append(line[:character_index])
            # 만약 지금 나타난 `.`이 마지막 문자라면 break
            if character_index == max_index :
                break
            # 저장된 앞 문장을 제외한 이후 인덱스부터 다시 시작
            line = line[character_index:]
            character_index = 0

    return lines

def main() :
    file = open(f".\sample.txt", "r", encoding="utf-8")
    line = file.readline()
    file.close()
    
    lines = processing(line)
    print(lines)
    
    file_out = open(f".\output.txt", "w", encoding="utf-8")
    for line in lines :
        print(line, file=file_out, end="\n")
        
if __name__ == "__main__" :
    main()