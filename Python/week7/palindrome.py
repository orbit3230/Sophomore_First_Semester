import string
from collections import namedtuple, deque

def isPalindrome_deque(str: string) -> bool:
    chars = deque(str)
    while len(chars) > 1:  # 하나만 남는 경우에도 확인할 필요 X
        if chars.popleft() != chars.pop():
            return False
    return True
    
def isPalindrome_list(str: string) -> bool:
    chars = list(str)
    start = 0
    end = len(chars) - 1
    while start < end:
        if chars[start] != chars[end]:
            return False
        start += 1
        end -= 1
    return True
    
def isPalindrome(str: string) -> namedtuple:
    result = namedtuple('Palindrome_Results', ['List', 'Deque'])
    return result(isPalindrome_list(str), isPalindrome_deque(str))
    
if __name__ == "__main__":
    inputs = input('Input a word (-1 to exit): ')
    while inputs != '-1':
        result = isPalindrome(inputs)
        print(result)
        inputs = input('Input a word (-1 to exit): ')
    print('Program exit')