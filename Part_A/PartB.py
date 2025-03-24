import unittest

from PartA import *





class Test(unittest.TestCase):
    # B2
    def test_instance(self):
        obj = Phone1
        self.assertIsInstance(obj, Phone)

    # B3
    def test_NOT_instance(self):
        obj = Phone2
        self.assertNotIsInstance(isinstance(obj, androidPhone), type(None))

class MyObject:
    def __init__(self, value):
        self.value = value

class TestObjectIdentity(unittest.TestCase):
    # B4
    def test_two_objects_identical(self):
        obj1 = Phone1
        obj2 = Phone2
        self.assertIs(obj1, obj2)



# B6
if __name__ == '__main__':
    unittest.main()