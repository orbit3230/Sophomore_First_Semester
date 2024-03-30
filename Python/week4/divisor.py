import time

# callback 인자를 무조건 받는자는 전제 하
# callback 함수의 작동 시간을 측정 및 결과 반환
def estimate_time_func(callback, n) :
    start = time.time()
    list = callback(n)
    end = time.time()
    return list, end-start

def find_divisor_list(n: int) :
    list = []
    for i in range(1, n+1) :
        if(n % i == 0) :
            list.append(i)
    return list
def find_divisor_genetator(n: int) :
    for i in range(1, n+1) :
        if(n % i == 0) :
            yield i
    
if __name__ == "__main__" :
    n = int(input("n: "))
    
    res_list, t1 = estimate_time_func(find_divisor_list, n)
    res_generator, t2 = estimate_time_func(find_divisor_genetator, n)
    
    print(f"find_divisor_list result: {res_list}")
    print(f"find_divisor_list time: {t1}")
    print(f"find_divisor_generator result: {res_generator}")
    print(f"find_divisor_generator time: {t2}")
    print(f"find_divisor_generator list(result): {list(res_generator)}")