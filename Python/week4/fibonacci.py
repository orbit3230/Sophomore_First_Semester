import time

# callback 인자를 무조건 받는자는 전제 하
# callback 함수의 작동 시간을 측정 및 결과 반환
def estimate_time_func(callback, n) :
    start = time.time()
    fibo = callback(n)
    end = time.time()
    if(fibo == None) :
        t = None
    else :
        t = end-start
    return fibo, t

def fibo_iter(n: int) :
    if(n < 0) :
        print("Wrong input!!!")
        return
    if(n == 0) :
        return 0
    if(n == 1 or n == 2) :
        return 1
    n_minus_1 = 1
    n_minus_2 = 1
    fibo = n_minus_1 + n_minus_2
    for i in range(3, n) :
        n_minus_1 = n_minus_2
        n_minus_2 = fibo
        fibo = n_minus_1 + n_minus_2
    return fibo

def fibo_recursive(n: int) :
    if(n < 0) :
        print("Wrong input!!!")
        return
    if(n == 0) :
        return 0
    if(n == 1 or n == 2) :
        return 1
    return fibo_recursive(n-1) + fibo_recursive(n-2)
    
if __name__ == "__main__" :
    n = int(input("n: "))
    
    res_iter, t1 = estimate_time_func(fibo_iter, n)
    res_recursive, t2 = estimate_time_func(fibo_recursive, n)
    
    print(f"fibo_iter result: {res_iter}")
    print(f"fibo_iter time: {t1}")
    
    print(f"fibo_recursive result: {res_recursive}")
    print(f"fibo_recursive time: {t2}")