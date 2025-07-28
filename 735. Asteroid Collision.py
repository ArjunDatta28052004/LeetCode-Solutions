class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for i in asteroids:
            while ans and i<0<ans[-1]:
                if ans[-1] < -i:
                    ans.pop()
                    continue
                elif ans[-1] == -i:
                    ans.pop()
                break
            else:
                ans.append(i)
        return ans
