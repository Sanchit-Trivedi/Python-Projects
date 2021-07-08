# CSE 101 - IP HW2
# K-Map Minimization 
# Name:Sanchit Trivedi
# Roll Number:2018091
# Section:A
# Group:3
# Date:19/10/2018


import unittest
from HW2_2018091 import *

class testpoint(unittest.TestCase):
	def test_minFunc(self):
		self.assertEqual(minFunc(4,"(0,1,2,3,13) d(5,7,9)"),"W'X' + Y'Z")
		self.assertEqual(minFunc(3,"(0,3,4,7) d(2,6"),"X + Y'")
		self.assertEqual(minFunc(4,"(0,1,2,4,5,7,9,10) d(3,8,15)"),"W'Y' + W'Z + X'Y' + X'Z'")
		self.assertEqual(minFunc(2,"(0,1) d(2)"),"W'")
		self.assertEqual(minFunc(4,"(0,1,2,5,6,7) d(11,13,15)"),"W'X'Y' + W'YZ' + XZ")
		self.assertEqual(minFunc(4,"(0,1,2,3,4,6,8,9,10,11,12,14) d(5,7,13,15)"),'1')
		self.assertIn(minFunc(3,"(0,1,2,5,6,7) d-"),["W'X' + WY + XY'","W'Y' + WX + X'Y"])#wikipedia petrick's example
		self.assertIn(minFunc(3,"(3,4,7) d(1,2,5,6"),["W + Y","W + X"])
		self.assertEqual(minFunc(2,"(1,2) d-"),"W'X + WX'")
		self.assertIn(minFunc(4,"(0,1,4,5,7,9,10,11,13,15) d-"),["W'Y' + WX'Y + WZ + XZ","W'Y' + WX'Y + XZ + Y'Z"] )
		
                
if __name__=='__main__':
	unittest.main()
