import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from matplotlib.pyplot import figure



for filename in os.listdir('png/'):
    if filename.endswith(".png") :
        img = mpimg.imread(filename)
        plt.figure(figsize=(18,12))
        imgplot = plt.imshow(img)
        plt.axis('off')
        plt.show(block=False)
        plt.pause(20)
        plt.close()
