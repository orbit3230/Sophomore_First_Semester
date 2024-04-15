import numpy as np

# main 함수
def main() :
    file = open(r".\inputfile.txt", "r")
    
    vectors_list = []   # vector들을 담을 리스트
    lines = file.readlines()
    for line in lines :
        words = line.split()
        vector = np.array([])
        for word in words :
            vector = np.append(vector, float(word))
        vectors_list.append(vector)
        
    # Gram-Schmide Algorithm
    checked, is_independent = gramSchmidt(vectors_list)
    
    print("Input vectors are linearly independent." if is_independent 
          else "Input vectors are linearly dependent.")
    print(f"The # of vectors had checked: {checked}")

# Gram-Schmidt Algorithm
def gramSchmidt(vectors) :
    orthonormal_list = []  # gramSchmidt 과정을 거친 orthonormal vector들을 담는 리스트
    current_index = 0      # 현재 확인하고 있는 vector의 index
    for a_i in vectors :   # a_i는 다음으로 확인할 i번째 
        # ---- (1) orthogonalization ----
        if(current_index == 0) :
            q_tilde = a_i
        else :
            q_tilde = orthogonalization(a_i, current_index, orthonormal_list)
            
        # ---- (2) Test for linear independence ----
        if(testing_linearly_independent(q_tilde)) :
            return current_index+1, False
        
        # ---- (3) Normalization ----
        q_i = normalization(q_tilde)
        orthonormal_list.append(q_i)
        current_index += 1
    
    return current_index, True

# i번째 vector a_i가 주어지면, 기존 orthonormal vector들과
# 직교하는 orthogonal vector q_tilde를 만드는 **Orthogonalization**
def orthogonalization(a_i, index, orthonormal_list) :
    q_tilde = a_i
    for i in range(index) :
        q_tilde -= np.inner(orthonormal_list[i], a_i) * orthonormal_list[i]
    return q_tilde

# orthogonal 시킨 q_tilde가 Zero Vector인지 확인하는 **Test for linear independence**
def testing_linearly_independent(q_tilde) :
    # q_tilde가 zero vector인지 확인 (code from stackoverflow)
    is_zeroV = np.allclose(q_tilde, np.zeros_like(q_tilde))
    return is_zeroV

# q_tilde의 norm값을 1로 만들어줌으로서
# orthonormal vector q_i를 만드는 **Normalization**
def normalization(q_tilde) :
    q_i = q_tilde / np.linalg.norm(q_tilde)
    return q_i
        
if __name__ == "__main__" :
    main()