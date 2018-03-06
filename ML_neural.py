from sklearn.neural_network import MLPClassifier
from PIL import Image
import os, sys
import numpy as np
import pickle
# drive_path="F:/Learnings/image magnification/training/actual/data"
drive_path="./150-100d"
train_path="./15_10"
# X = [[0., 0.], [1., 1.]]
# y = [[0, 1], [1, 1]]
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(15,), random_state=1)
# clf.fit(X, y)
# print(clf.predict([[2., 2.], [-1., -2.]]))
# Z= [[2., 1.]]
# clf.fit(Z,[[2,3]])
# print(clf.predict([[2., 2.], [-1., -2.]]))



# import nltk
# import sklearn
#
# print("Start")
# print('The nltk version is {}.'.format(nltk.__version__))
# print('The scikit-learn version is {}.'.format(sklearn.__version__))
# print("Done")


def getfileList():
    filename_array=[]
    for root, dirs, files in os.walk(train_path):
        for filename in files:
            # print(filename)
            # filename=files[0]
            filename_array.append(filename)
    print(filename_array)
    return filename_array

def convertBlackWHite(image_file):
    return image_file.convert('1')
# convert image to black and white

# def save(image_file,filename):
#     return image_file.save(filename,'JPEG')

def openfile(filename):
    return Image.open(filename)

def gettrainingset(filename_array):
    im_train_data=[]
    im_train_result = []
    for filename in filename_array:
        print(filename)
        im_train = Image.open(train_path + "/" + filename)
        im_train=convertBlackWHite(im_train)

        im_result= Image.open(drive_path + "/" + filename)
        im_result = convertBlackWHite(im_result)

        # print(list(np.array(im_result).flat))
        # print(im_train)
        # print(list(np.array(im_train).flat))
        im_train=list(np.array(im_train).astype(int).flat)
        im_result = list(np.array(im_result).astype(int).flat)


        # im_result=list(np.array(im_train).flat)
        im_train_result.append(im_result)
        im_train_data.append(im_train)

    return (im_train_data,im_train_result)

def savpickle(name,data):
    with open(name+'filenamelearn.pickle', 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
fileList=getfileList()
fileTrain=fileList[0:400]
fileTest=fileList[400:]
tt,result=gettrainingset(fileTrain)
savpickle("Train_data_",tt)
savpickle("Train_result_",result)
print("Started training")
clf.fit(tt,result)
savpickle("clf_",clf)
# output=clf.predit(fileTest)
# savpickle("output_",output)
