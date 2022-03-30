#!/usr/bin/env python
# coding: utf-8

# In[2]:


import zipfile as zf
files=zf.ZipFile("UrbanSound8K.zip",'r')

files.extractall("UrbanSound8K")
files.close()


# In[ ]:




