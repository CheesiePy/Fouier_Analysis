import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import time

# --- part 1 ---
def create_sin(seconds, fs, freq):
    x = np.arange(0, seconds, 1/fs)
    return np.sin(2 * np.pi * x * freq)

def create_tone(seconds, fs, freqs):
    return sum(map(lambda freq: create_sin(seconds, fs, freq), freqs))

def play_tone(seconds, fs, freqs):
    tone = create_tone(seconds, fs, freqs)
    sd.play(tone, fs)
    time.sleep(seconds)
    sd.stop()
# --- end part 1 ---


# --- part 2 ---
## grand-shmitd process

def gram_schmidt_process(matrix): 
    # @param: matrix = linearly independent set of vectors
    # returns  retmatrix of orthonormal vectors as columns

    dtype = np.float64 # set the data type
    ret_matrix = np.zeros(matrix.shape, dtype=dtype) # initialize return matrix as zeros

    for i in range(matrix.shape[1]): # for each column
        ret_matrix[:,i] = matrix[:,i] # copy the  vector to the return matrix

        for j in range(i): # for each previous vector
            ret_matrix[:,i] -= (ret_matrix[:,j] @ matrix[:,i]) * ret_matrix[:,j] # subtract the projection of the vector onto the previous vectors
    

        ret_matrix[:,i] /= np.linalg.norm(ret_matrix[:,i]) # normalize the vector

    return ret_matrix # return the matrix of orthonormal vectors
    # -- end part 2 ---

def main():
    # --- part 1 ---
    #play_tone(1, 44100, (1209, 697))


    # --- part 2 ---

    matrix = np.array([[1, 2, 3], [-1, 0, -3], [0, -2, 3]])
    norm_mat = gram_schmidt_process(matrix)
    print(norm_mat)
    
main()




