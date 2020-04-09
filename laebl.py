import numpy as np
from PIL import Image
import pickle
import matplotlib.pyplot as plt

img = dict()
img_n = dict()
for i in range(0,64):
    img[i]= Image.open(r"C:\Users\sen\Desktop\24cell_data\\"+str(i)+".png")
    img_n[i] = np.array(img[i])
plt.imshow(img[1])
plt.show()
print(type(img_n[2]))
image_data =[]
for i in range(0,64):
    image_data.append(img_n[i])
image_label = np.empty(64)
for i in range(0,37):
    image_label[i]=0
for i in range(37,64):
    image_label[i] = 1




image_data = np.array(image_data)
image_label = image_label.astype(np.int)
print(image_label)
train_data =(image_data,image_label)



write_file=open(r'C:\Users\sen\Desktop\24cell_data_data1.pkl','wb')
pickle.dump(train_data,write_file)
write_file.close()

read_file=open(r'C:\Users\sen\Desktop\24cell_data_data1.pkl','rb')

(train_data,lab_data)=pickle.load(read_file)
read_file.close()

print(type(train_data))
print(train_data.shape)
print(lab_data)

plt.imshow(train_data[0])
plt.show()
