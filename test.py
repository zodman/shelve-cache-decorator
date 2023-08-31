import unittest
import shelve_cache_decorator
import datetime


class Test(unittest.TestCase):
    def test_one(self):
        exp = datetime.timedelta(seconds=5) 
        @shelve_cache_decorator.shelvecached('/tmp/a', exp)
        def l(a):
            return a
        self.assertEqual('b1',l('b1'))



if __name__ == "__main__":
    unittest.main()
