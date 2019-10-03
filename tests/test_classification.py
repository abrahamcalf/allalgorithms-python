import unittest
from allalgorithms.classification import nearest_neighbor

class TesteClassifications(unittest.TestCase):

    def test_nn(self):
        #datas
        #the first data is Weight and second is number of wheels
        features = [
            [110,2],
            [125,2],
            [100,2],
            [110,2],
            [300,4],
            [278,4],
            [290,4],
            [260,4],
        ]
        #labels, the labels is classification of features line
        #in this exemple 0 = Motorcicler, 1 = car
        label = [
            0,
            0,
            0,
            0,
            1,
            1,
            1,
            1,
        ]
        #instance classifier
        clf = nearest_neighbor.NN()
        #treaning
        clf = clf.fit(features,label)
        #predict
        rs = clf.predict([[2,115]])
        self.assertEqual(rs,0)
    
if __name__ == "__main__":
    unittest.main()