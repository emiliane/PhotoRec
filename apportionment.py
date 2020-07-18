from os import listdir
from os.path import isfile, join
import os
import shutil

path = '/media/ubuntu/USB DISK/7/'
newpath = '/media/ubuntu/USB DISK/new/'

for d in listdir(path):
    mypath = path + d

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    for f in onlyfiles:
        filename, file_extension = os.path.splitext(f)

        folder = newpath + '7' + file_extension
        if not os.path.exists(folder):
            os.makedirs(folder)

        ff = mypath + '/' + f
        fff = folder

        print('move ' + ff + ' to ' + fff)
        shutil.move(ff, fff)
