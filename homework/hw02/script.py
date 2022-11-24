from hw02 import *

def main():
    flag = True
    face = make_face()
    trys = 0
    while flag:
        plt.imshow(face, cmap='gray')
        #plt.show() - og face
        rand = np.random.randint(2, size=(6,6))
        randface = np.zeros((8,8))
        randface[1:7, 1:7] = rand[:,:]
        plt.imshow(randface, cmap='gray')
        sim = similarity(face,randface)
        stitle = "the similarity is :" + "{:.2f}".format(sim)
        plt.title(stitle)
        #plt.show() - rand face
        if sim > 0.7:
            print("access permitted")
            plt.title(stitle + " number of trys {0}".format(trys))
            plt.show()
            break
        else:
            print("access denied" + f"number of trys {trys}")
            trys += 1

main()    