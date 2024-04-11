import numpy as np

def main() :
    file = open(r".\input.txt", "r")
    
    lines = file.readlines()
    for line in lines :
        words = line.split()
        vector = np.array([])
        for word in words :
            vector = np.append(vector, float(word))
        
def gramSchmidt(vector) :
    # TODO: Implement this function
    None
        
if __name__ == "__main__" :
    main()