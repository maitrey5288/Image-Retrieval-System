'''
To find list of images in temp folder
these are images uploaded by user

'''


import os 
def imagelist(path):
    res= []
    # print(os.listdir())
    for file in os.listdir(path):
        # check only text files
        if file.endswith('.png') or file.endswith('.jpg') :
            res.append(file)
    return res

print(imagelist('static/images/'))
print(os.listdir('static/images'))

