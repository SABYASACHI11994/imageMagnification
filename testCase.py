import numpy as np
import pickle
from sklearn.neural_network import MLPClassifier
from PIL import Image

drive_path="./150-100d"
train_path="./15_10"
filename="DSC_2360.jpg"
def convertBlackWHite(image_file):
    return image_file.convert('1')

with open('clf_filenamelearn.pickle', 'rb') as handle:
    clf = pickle.load(handle)

im_train = Image.open(train_path + "/" + filename)

im_train=convertBlackWHite(im_train)

im_result= Image.open(drive_path + "/" + filename)
im_result = convertBlackWHite(im_result)

# print(list(np.array(im_result).flat))
# print(im_train)
# print(list(np.array(im_train).flat))
im_train_result=[]
im_train_data=[]
im_train=list(np.array(im_train).astype(int).flat)
im_result = list(np.array(im_result).astype(int).flat)
im_train_result.append(im_result)
im_train_data.append(im_train)
x=clf.predict(im_train_data)
print(x[0])
print(im_result)
j=np.array([c==1 for c in x[0]])
j2d=  np.reshape(j, (-1, 150))
print(j2d)
im = Image.fromarray(j2d)
print(im)
im.save("Test_"+filename, "JPEG")
im.show()
