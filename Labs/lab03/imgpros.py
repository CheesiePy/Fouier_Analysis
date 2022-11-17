import matplotlib.image
import matplotlib.pyplot as plt
import numpy as np

img = matplotlib.image.imread("Labs/lab03/colors.png")

print(type(img)) # numpy.ndarray

# print(img.ndim == len(img.shape))  
print(img.shape) # 3dim

# plt.imshow(img)
# plt.show()

# plt.imshow(img)
# plt.show()

#.7 show rgba channels one each chammel .
for i in range(3):
    plt.imshow(img[:,:,i], cmap='gray')
    #plt.show()

#.8
# changing the 
img[:,:,3] = np.random.uniform(size=(1000,1000))
plt.imshow(img[:,:,3], cmap='gray')
#plt.show()
plt.imshow(img)
#plt.show()

#.9
# rgba -> rgb
img = img[:,:,:3]
plt.imshow(img)
#plt.show()

#10. do 180deg on the y-axis
plt.imshow(img[::-1, :,:])
#plt.show()


#11. do a 180deg on the x-axis
plt.imshow(img[:,::-1,:], cmap='gray')
#plt.show()

#12.
plt.imshow(img[:,:,0].T, 'gray')
#plt.show()

#13.
z_img = np.zeros(img.shape)
print(z_img.shape)

#14.
z_img[:,:,0] = img[:,:,0].T
#15.
z_img[:,:,1] = img[:,::-1,1]
#16
z_img[:,:,2] = img[::-1,:,2]
#17
plt.imshow(z_img)
#plt.show()
#18
plt.imshow((img[1:,:,:]- img[:-1,:,:]))
#plt.show()
#19
plt.imshow((img[:,1:,:] - img[:,:-1,:]))
#plt.show()

#20
plt.imshow((img[1:,1:,:] - img[:-1,:-1,:]))
#plt.show()



#21 divide all colors channels by 3 and sum them up
plt.imshow(np.sum(img/3, axis=2), cmap='gray')
#plt.show()

#same as get the mean of all three color channels
plt.imshow(np.mean(img, axis=2), cmap='gray')
#plt.show()

#22
img_1 = img[::, ::-1,::] ** img[::-1, :: ,::] - img[::-1,:,:]
img_2 = img[::,::,::-1] + img[::,::-1,::]
img_3 = np.dstack((img_1, np.ones((1000,1000)) * 0.3))
img_4 = np.dstack((img_2, np.ones((1000,1000)) * 0.7))
plt.imshow( img_4 ** img_3)
plt.show()