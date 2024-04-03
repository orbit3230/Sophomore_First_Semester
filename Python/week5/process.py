def processing(line) :
    max_index = len(line)   # 문자열의 길이(마지막 인덱스 + 1)
    line_upper = ""         # 문자열을 대문자로 변환한 것
    lines = []              # 문자열을 문장 단위로 나눈 것을 담은 리스트
    next_character = ''     # 다음 문자
    character_index = 0     # 현재 문자의 인덱스
    split_point = 0         # 문장을 나누었던 포인트 인덱스
    # 우선 모든 문자들을 대문자로 변환(alphabetical 한 문자만을 대상으로)
    for character in line :
        if 'a' <= character and character <= 'z' :
                line_upper += chr(ord(character) - 32)
        else :
            line_upper += character
    
    # '.'을 기준으로 나누고 각 문장들을 배열(lines)에 저장    
    for character_index in range(max_index):
        next_character = line_upper[character_index]
        # 만약 '.'을 만나면
        if next_character == '.' :
            # 처음부터 `.`이 처음 나타난 곳 까지를 한 문장으로 배열에 저장
            lines.append(line_upper[split_point:character_index+1])
            # 다음 단어부터는 다음 줄(배열 인덱스)에 저장
            split_point = character_index+1

    return lines

def main() :
    file = open(r".\sample.txt", "r", encoding="utf-8")
    line = file.readline()
    file.close()
    
    lines = processing(line)
    print(lines)
    
    file_out = open(r".\output.txt", "w", encoding="utf-8")
    for line in lines :
        print(line, file=file_out, end="\n")
        
if __name__ == "__main__" :
    main()