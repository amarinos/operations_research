import os
import unittest
import sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
from distance_api.distance_matrix import create_distance_matrix, define_distance_matrix
from constants import api_key

addresses =  ["SanFrancisco,CA,USA", "Vancouver,BC,Canada", "Seattle,WA,USA"]
addresses_2= ['Essen+Germany', #0
                       'Dusseldorf+Germany', #1
                       'Stuttgart+Germany', #2
                       'Berlin+Germany',  #3
                       'Hamburg+Germany', #4
                       'Duisburg+Germany', #5 
                       'Salzburg+Austria', #6
                       'Munich+Germany', #7
                       'Aachen+Germany', #8
                       'Dresden+Germany', #9
                       'Saarland+German' #10
                      ]
class PositionSummaryTests(unittest.TestCase):

    def test_number_1(self):
        self.assertEqual(type(create_distance_matrix(addresses, api_key)), list)
        self.assertEqual(type(define_distance_matrix(addresses, api_key)), list)

    def test_number_2(self):
        self.assertEqual(type(create_distance_matrix(addresses_2, api_key)), list)
        self.assertEqual(type(define_distance_matrix(addresses_2, api_key)), list)


if __name__ == "__main__":
    unittest.main()