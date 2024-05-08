import random

def generate_three_list() :
    l1 = [random.randrange(11) for i in range(10)]
    l2 = [random.randrange(11) for i in range(10)]
    l3 = [random.randrange(11) for i in range(10)]
    return l1, l2, l3

def calculate_lists(l1, l2, l3) :
    zip_list = list(zip(l1, l2, l3))
    max_list = [max(i) for i in zip_list]
    min_list = [min(i) for i in zip_list]
    return max_list, min_list
    
if __name__ == "__main__" :
    l1, l2, l3 = generate_three_list()
    print(f"l1: {l1}")
    print(f"l2: {l2}")
    print(f"l3: {l3}")
    print("="*40)
    
    max_list, min_list = calculate_lists(l1, l2, l3)
    
    print(f"max_list: {max_list}")
    print(f"min_list: {min_list}")