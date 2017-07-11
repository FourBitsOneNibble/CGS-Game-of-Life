import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def setUp(self):
        print('\nsetup')

    def tearDown(self):
        print('tear down')


if __name__ == '__main__':
    unittest.main()
