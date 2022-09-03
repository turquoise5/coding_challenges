class Solution:
    def reverseString(self, s: List[str]) -> None:
        b = []
        for t in s:
            b += t
        for i in range(len(s)):
            s[i] = b[len(b)-i-1]
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if nums[i] * nums[j] == target:
                    print(nums[i], nums[j])
                    return [i, j]

def findExit(intLi):
    hops = 0
    if intLi == []:
        return False
    if len(intLi) == 2:
        hops = intLi[0]
    else:
        while hops < len(intLi)-1:
            hops = hops + intLi[hops]
            if hops >= len(intLi):
                return False
            if hops == 0:
                return False
            if intLi[hops] == 0:
                return False
            if intLi[0] < 0:
                return False
        
    if hops == len(intLi)-1:
            return True
    else:
            return False