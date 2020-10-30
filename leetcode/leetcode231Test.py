import unittest
from leetcode.leetcode231 import Solution


class MyTestCase(unittest.TestCase):
    def test_isPowerOfTwo(self):
        s = Solution()
        self.assertEqual(s.isPowerOfTwo(1), True)
    def test_isPowerOfTwo2(self):
        s = Solution()
        self.assertEqual(s.isPowerOfTwo(16), True)
    def test_isPowerOfTwo3(self):
        s = Solution()
        self.assertEqual(s.isPowerOfTwo(218), False)

if __name__ == '__main__':
    unittest.main()
