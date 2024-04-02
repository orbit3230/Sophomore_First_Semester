import numpy as np

## r은 raw string을 의미한다. '\'를 있는 그대로 인식.
filename = open(r'.\inputfile.txt', 'r')
k = int(input())
iteration = int(input())

vectors_set = []

lines = filename.readlines()
for line in lines:
    words = line.split(' ')
    vector = np.array([])
    for word in words :
        np.append(vector, int(word))
    vectors_set.append(vector)

# 초기 대표값 설정(vector들 중 하나로)
representatives = []
for i in range(k) :
    representatives.append(vectors_set[i])

for iter in range(iteration) :
    group = []
    for i in range(k) :
        new_group = []
        group.append(new_group)
    for v in vectors_set :
        group[np.argmin([np.linalg.norm(r-v) for r in representatives])].append(v)

    representatives = []
    for i in range(k) :
        r = np.array([])
        sum = [0, 0, 0, 0, 0]
        for g in group[i] :
            index = 0
            for j in g :
                sum[index] += j
                index += 1
        for l in range(5) :
            np.append(r, sum[l]/len(group[i]))
        representatives.append(r)
        
print(representatives)