from math import sqrt

class KNN():
    """
    This is my first classifier :)
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
            print(dist,best_distance, best_index)
        return self.labels[best_index]