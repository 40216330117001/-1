# -*- coding: utf-8 -*-
"""student2(class).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aqcTZmUxxI3AhEeVWM8JllBFbhULz8Vw
"""

class student:
  def __init__(self,id,name):
    self.id=id
    self.name=name

  def __del__(self) :
    print(self.name,"Deleted")

  def mean(self):
    sum=0
    vs=0
    input()
    return sum/vs

  def is_mashroot(self):
    if self.mean()<12:
      return True
    else:
      return False

  def __str__(self):
    print("this class is student")