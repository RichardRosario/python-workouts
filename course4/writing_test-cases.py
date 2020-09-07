import unittest


class EqualityTest(unittest.TestCase):

    def testEqual(self):
        self.assertEqual(1, 3-2)

    def testNotEqual(self):
        self.assertNotEqual(2, 3-2)

    def square(self):
        self.assertEqual(3, 9)


if __name__ == '__main__':
    unittest.main()


# side effect test ... set up known value.. and see if value is updated correctly
def distance(x1, y1, x2, y2):
    dx = x1-x2
    dy = y1-y2
    d = dx**2 + dy**2
    result = d**0.5
    return result


assert distance(3, 2, 3, 3) == 1
