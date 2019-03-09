#program to list all files in a directory

from os import walk


for filenames in walk('/home/bridgeit'):

 print(filenames)
