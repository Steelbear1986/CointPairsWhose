class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        j=1
        dlina=len(nums)
        answer=[ 1  for y  in range(dlina-1) for j in range(y, dlina) if nums[y]+nums[j]<target and y<j]
        return  sum(answer)