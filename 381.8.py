# Problem 8

# Write and test a function removeDuplicates(somelist) that removes duplicate values from a list

import unittest

def removeDuplicates(somelist):
    newlist = []
    for num in somelist:
        if num not in newlist:
            newlist.append(num)
    return newlist

class MyTest(unittest.TestCase):

    def test_Middle(self):
        # Multiples in middle
        self.assertEqual(removeDuplicates([1,2,2,3]), [1,2,3])

    def test_Empty(self):
        # empty list
        self.assertEqual(removeDuplicates([]), [])

    def test_One(self):
        # One item in list
        self.assertEqual(removeDuplicates([1]), [1])

    def test_no_Multiples(self):
        # No multiples
        self.assertEqual(removeDuplicates([1,2,3,4]), [1,2,3,4])

    def test_Only(self):
        # Only multiples
        self.assertEqual(removeDuplicates([2,2,2,2]), [2])

    def test_Beginning(self):
        # Multiples at beginning
        self.assertEqual(removeDuplicates([5,5,7,8]), [5,7,8])

    def test_End(self):
        # Multiples at end
        self.assertEqual(removeDuplicates([1,2,6,6]), [1,2,6])


