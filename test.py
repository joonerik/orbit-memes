import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from matplotlib.pyplot import figure



for filename in os.listdir('../Memes'):
    if filename.endswith(".png") or filename.endswith(".jpg") :
        img = mpimg.imread(filename)
        plt.figure(figsize=(13,8))
        imgplot = plt.imshow(img)
        plt.axis('off')
        plt.show(block=False)
        plt.pause(5)
        plt.close()
