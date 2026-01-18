class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # index to place the next kept element

        for x in nums:
          if x != val:
              nums[k] = x
              k += 1

        return k

#alternative

nums = [0,1,2,2,3,0,4,2]
vals = 3

def removeElement(nums, vals):
    x=0
    for i in nums:
        if nums[x] == vals:
            nums[x] = 0
        x+=1
    return nums


new_list = [1,2,2]
num = 2
removeElement(new_list, num)
