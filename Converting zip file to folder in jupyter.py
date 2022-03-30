#!/usr/bin/env python
# coding: utf-8



import zipfile as zf
files=zf.ZipFile("UrbanSound8K.zip",'r')

# In the place of urbansound8k.zip write the zip file name that you uploaded in the jupyter 

# In the place of urbansound8k in the below , kinldy write the name of the folder you want to keep after extraction 

files.extractall("UrbanSound8K")
files.close()





