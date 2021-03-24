#!/usr/bin/env python
# coding: utf-8

# In[11]:


radius = float(input("Enter radius of the circle:"))
print(radius)
import math 
math.pi
area = math.pi * radius * radius
print(area)
fn= input("Enter Filename: ")
f = fn.split(".")
print ("Extension of the file is : " + repr(f[-1]))


# In[ ]:




