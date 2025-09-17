class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L = 1
        R = num

        while L <= R:
            M = (L + R) // 2
            m_squared = M ** 2
            if num == m_squared:
                return True
            elif num > m_squared:
                L = M + 1
            else:
                R = M - 1

        return False
        