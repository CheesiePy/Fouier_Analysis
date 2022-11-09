import numpy as np
c = complex


def main():
    # matracies 
    A = np.array([[1,1,0],[1,-2,1],[2,1,2]])
    B = np.array([[1,-1,1],[-1,0,1],[3,2,1]])
    C = np.array([[c(1, 0),c(0, -1)],[c(-1, 0),c(0, 1)],[c(0, 0),c(0, 2)]])

    # vectors
    x = np.array([1,2,-2]).transpose()
    y = np.array([2,-1,3])

    # q1.1
    print("A*x :\t", A@x, end="\n--------------\n")
    print("B@x@C :\t",  B@x@C, end="\n--------------\n")
    print("(y@A)@B :\t", (y@A)@B, end="\n--------------\n")
    print("C@np.transpose(C)@x :\t", C@np.transpose(C)@x,  end="\n--------------\n")
    print("x@y :\t" , y@x,  end="\n--------------\n")


    # q1.2

    print("A+B using the + oprator:\n", A+B, end="\n--------------\n")
    print("A+B using the np.add() function:\n", np.add(A,B), end="\n--------------\n")

main()