# -*- coding: UTF-8 -*-
#
# Nearest neighbour classifier one entry
# The All ▲lgorithms library for python
#
# Contributed by: Carlos Abraham Hernandez
# Github: @abranhe
#

from math import sqrt

class NN():
    """
    Nearest neighbour classifier for two-dimensional dataset
    """
    def fit(self,data,labels):
        self.data = data
        self.labels = labels
        
        return self
    
    def predict(self,x_test):
        predicts = []
        for row in x_test:
            label = self.closest(row)
            predicts.append(label)
        return predicts
    
    def euc(self,a,b):
        return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
            
    
    def closest(self,row):
        #initial best distance is alwas first
        best_distance = self.euc(row,self.data[0])
        best_index = 0
        #intering in data
        for i in range(1,len(self.data)):
            dist = self.euc(row,self.data[i])
            if dist < best_distance:
                best_distance = dist
                best_index = i
        return self.labels[best_index]