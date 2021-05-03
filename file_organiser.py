
''' Import libraries '''
import os
import shutil
from os import listdir
from os.path import isfile, join
import tkinter as tk
from tkinter import filedialog
from tkinter import *



print('This is a program that organises files in a given directory')
print(''
      
      '')

print('Please select the folder in which you want to organise your files')

print(''
      
      '')

''' Source Folder '''

root = Tk()
root.withdraw()

source_path = filedialog.askdirectory()

''' Create destination folders in the source folder '''
newpath1 = os.path.join(source_path, 'Images')
if not os.path.exists(newpath1):                     # check to see if they already exist
    os.makedirs(newpath1)

newpath2 = os.path.join(source_path, 'Documents')
if not os.path.exists(newpath2):
    os.makedirs(newpath2)

newpath3 = os.path.join(source_path, 'Else')
if not os.path.exists(newpath3):
    os.makedirs(newpath3)


''' Moving the files '''
files = [file for file in listdir(source_path) if isfile(join(source_path,file))]

for file in files:
    if file.endswith(('.JPG', '.png', '.jpg')):
        shutil.move(os.path.join(source_path,file), os.path.join(newpath1,file))
    elif file.endswith(('.pdf', '.pptx', '.ppt', '.csv', '.xlsx', '.docx', '.doc')):
        shutil.move(os.path.join(source_path,file), os.path.join(newpath2,file))
    else:
        shutil.move(os.path.join(source_path,file), os.path.join(newpath3,file))

print("Your files have been moved!")
print(''
      
      '')

print("Please exit the program manually.")

if __name__ == '__main__':
    root.mainloop()





