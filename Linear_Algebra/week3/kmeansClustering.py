import numpy as np

## r은 raw string을 의미한다. '\'를 있는 그대로 인식.
filename = open(r'.\inputfile.txt', 'r')
k = int(input("# of groups, i.e., k = "))
iteration = int(input("# of actual iterations : "))

vectors_set = []

# vector set 제작
lines = filename.readlines()
for line in lines:
    words = line.split(' ')
    vector = np.array([])
    for word in words :
        # numpy append 함수는 기존 리스트에는 영향없이, 새 리스트를 반환하므로 assign 해주어야함.
        # 입력되는 vector 값은 int라고 가정
        vector = np.append(vector, float(word))
    # 다만 배열 append 함수는 기존 리스트에 영향을 준다.
    vectors_set.append(vector)
    
# vector들이 몇 차원인지 확인
# 문제에서는 5-vector로 제한을 두었지만, 프로그램의 확장성을 위해.
dimension = len(vectors_set[0])

# 초기 대표값 설정(vector들 중 하나로)
# 만약 대표값의 개수가 vector의 개수보다 많다면 문제가 되겠지만, 그럴 일은 없다고 가정.
representatives = []
for i in range(k) :
    representatives.append(vectors_set[i])

# k-means clustering iteration 수행
actual_iteration = 0
for actual_iteration in range(iteration) :
    # 각각의 vector들을 가장 가까운 representative에 매칭.
    group = []
    for i in range(k) :
        new_group = []
        group.append(new_group)
    for v in vectors_set :
        # norm 값에 제곱을 취하지 않았음(결과에 영향이 없기 때문)
        group[np.argmin([np.linalg.norm(r-v) for r in representatives])].append(v)

    # 각 대표값 그룹에 속한 vector들의 평균값(중간 좌표)를 새로운 대표값으로 설정.
    old_representatives = representatives  # 만약 대표값이 변하지 않았는지 확인하기 위해 임시로 저장
    representatives = []
    for i in range(k) :
        r = np.array([])
        sum = [0] * dimension
        for g in group[i] :
            index = 0
            for j in g :
                sum[index] += j
                index += 1
        for l in range(dimension) :
            # 드물지만, 해당 대표값에 속한 그룹이 아예 없을 경우에
            # 랜덤하게 대표값을 새로 설정해준다.
            # 랜덤하게 정해주는 건 좋은 방식은 아닌 것 같지만, 우선 이렇게 설정해주겠다.
            if(len(group[i]) == 0) :
                r = vectors_set[np.random.randint(0, len(vectors_set))]
                break
            r = np.append(r, sum[l]/len(group[i]))
        representatives.append(r)
        
    # 대표값이 변하지 않았다면, iteration을 종료.
    is_all_same = True
    for i in range(k) :
        if(np.array_equal(old_representatives[i], representatives[i]) == False) :
            is_all_same = False
            break
    if(is_all_same) :
        break

# 결과 출력
print("# of actual iteration : ", actual_iteration + 1)
print(representatives)
# 파이썬에서는 for 문 내에서 선언한 변수에 밖에서도 접근 가능함.
for i in range(k) :
    print("# of vectors in cluster %d : %d" % (i+1, len(group[i])))