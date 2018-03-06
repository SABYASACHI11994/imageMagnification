# # import numpy as np
# # from PIL import Image
# # #
# # # im = Image.open("picture.jpg")
# # # pix = np.array(im)
# # # print(len(pix),len(pix[1]))
# # # print(pix[0])
# # #
# # def convertBlackWHite(image_file):
# #     return image_file.convert('1')
# # # # convert image to black and white
# # #
# # def save(image_file,filename):
# #     return image_file.save(filename,'JPEG')
# # #
# # def open(filename):
# #     return Image.open(filename)
# # #
# # image=open("black1.jpg")
# # image=convertBlackWHite(image)
# # save(image,"black12.jpeg")
# # image=open("black12.jpeg")
# # x=np.array(image)
# # print(len(x),len(x[1]))
# # print(x[0])
# #
# # # # import pickle
# # # #
# # # # your_data = {'foo': 'bar'}
# # # #
# # # # # Store data (serialize)
# # # # with open('filename.pickle', 'wb') as handle:
# # # #     pickle.dump(your_data, handle, protocol=pickle.HIGHEST_PROTOCOL)
# # # #
# # # # # Load data (deserialize)
# # # # with open('filename.pickle', 'rb') as handle:
# # # #     unserialized_data = pickle.load(handle)
# # # #
# # # # print(your_data == unserialized_data)
# # #
# # # x=[1,2,3,4,5]
# # # print(x[1:3])
#
x=[1,2,3,4]
print([c==4 for c in x])