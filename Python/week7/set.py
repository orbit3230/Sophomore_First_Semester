# 집합에 ×원소를 더하여 반환하는 함수
def set_add(set, x) : 
    if(x not in set) :
        set.append(x)
    return set

# 집합에 여려개의 원소(List)를 업데이트 하여 반환하는 함수
def set_update(set, list) :
    for i in list :
        set = set_add(set, i)
    return set
        
# list를 집합으로 반환하는 함수
def set_generate(list) :
    set = []
    set = set_update(set, list)
    return set

# 빈 집합을 반환하는 함수
def set_clear(set) :
    return []

# 집합에서 × 원소를 제거하여 반환하는 함수
def set_remove(set, x) :
    if(x not in set) :
        print(f"{x} not in {set}")
        return set
    set.remove(x)
    return set

# 집합에서 × 원소를 제거하여 반환하는 함수
def set_discard(set, x) :
    if(x in set) :
        set.remove(x)
    return set

def main() :
    list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    set = set_generate(list)
    print(f'set_generate(list): {set}')

    set = set_add(set, 1)
    print(f'set_add(set, 1): {set}')

    set = set_add(set, 6)
    print(f'set_add(set, 6): {set}')

    set = set_update(set, [5,6,7,8])
    print(f'set_update(set, [5,6,7,8]): {set}')

    set = set_remove(set, 5)
    print(f'set_remove(set, 5): {set}')

    set = set_remove(set, 5)
    print(f'set_remove(set, 5): {set}')

    set = set_discard(set, 5)
    print(f'set_discard(set, 5): {set}')

    set = set_clear(set)
    print(f'set_clear(set): {set}')
    
if __name__ == '__main__' :
    main()