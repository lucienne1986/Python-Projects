import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")
print(df.shape)
M = df.as_matrix()
im = M[0, 1:]
print(im.shape)
im = im.reshape(28, 28)
im.shape

plt.imshow(im)
#plt.show() #show map in colours

#do display image in black and white
plt.imshow(im, cmap='gray')
