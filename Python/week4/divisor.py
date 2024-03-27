import time

def estimate_time_func(callback, n) :
    None
def find_divisor_list(n: int) :
    None
def find_divisor_genetator(n: int) :
    None
if __name__ == "__main__" :
    n = int(input("n: "))
    
    res_list, t1 = estimate_time_func(find_divisor_list, n)
    res_generator, t2 = estimate_time_func(find_divisor_genetator, n)
    
    print(f"find_divisor_list result: {res_list}")
    print(f"find_divisor_list time: {t1}")
    print(f"find_divisor_generator result: {res_generator}")
    print(f"find_divisor_generator time: {t2}")
    print(f"find_divisor_generator list(result): {list(res_generator)}")