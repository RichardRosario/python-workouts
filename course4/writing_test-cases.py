import unittest


class EqualityTest(unittest.TestCase):

    def testEqual(self):
        self.assertEqual(1, 3-2)

    def testNotEqual(self):
        self.assertNotEqual(2, 3-2)

    def testSquare(self, n):
        result = n*n
        self.assertEqual(3, 9)


if __name__ == '__main__':
    unittest.main()


# side effect test ... set up known value.. and see if value is updated correctly


# assert distance(3, 2, 3, 3) == 1
