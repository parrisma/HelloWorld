import unittest

from helloworld.HelloWorld import hello_world


#
# Execute the Hello World Tests
#

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        res = hello_world("Hello World", 1)
        self.assertEqual(res, 1)


if __name__ == "__main__":
    tests = TestHelloWorld()
    suite = unittest.TestLoader().loadTestsFromModule(tests)
    unittest.TextTestRunner().run(suite)
