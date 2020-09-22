from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            ans.extend(matrix[0])
            matrix = list(zip(* matrix[1:]))[::-1]
        return ans


if __name__=="__main__":
    # s = Solution()
    # print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print()
