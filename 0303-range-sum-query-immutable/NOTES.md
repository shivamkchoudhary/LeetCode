M-1:
​
class NumArray:
​
def __init__(self, nums: List[int]):
temp = 0
self.pre_sum = []
for i in nums:
temp += i
self.pre_sum.append(temp)
​
def sumRange(self, left: int, right: int) -> int:
if left == 0:
return self.pre_sum[right]
else:
return self.pre_sum[right] - self.pre_sum[left-1]
m-2 :
​
class NumArray:
​
def __init__(self, nums: List[int]):
self.nums = nums
​
def sumRange(self, left: int, right: int) -> int:
return sum(self.nums[left:right+1])
​
​
​
​
​
​