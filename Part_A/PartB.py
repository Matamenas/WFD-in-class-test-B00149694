import unittest

class MyClass:
    pass

class anotherClass:
    pass


class Test(unittest.TestCase):
    # B2
    def test_instance(self):
        obj = MyClass()
        self.assertIsInstance(obj, MyClass)

    # B3
    def test_NOT_instance(self):
        obj = anotherClass()
        self.assertNotIsInstance(isinstance(obj, MyClass), type(None))

class MyObject:
    def __init__(self, value):
        self.value = value

class TestObjectIdentity(unittest.TestCase):
    # B4
    def test_two_objects_identical(self):
        obj1 = MyObject(10)
        obj2 = obj1
        self.assertIs(obj1, obj2)


# B6
if __name__ == '__main__':
    unittest.main()