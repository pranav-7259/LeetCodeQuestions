#Since the majority element occurs more than half of time, the count of that element will be greater than all the other elements combined
#Algorithm -> count = 0, keep 1st element = nums[0] as result
#Now if you see the same number as result, increment by 1, else decrement by 1
#If your count becomes -1, which indicates that there are more number of other elements than your result,
#Update the result to the latest other element and make count = 1


from collections import Counter
from math import floor

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        result = nums[0]
        count = 0

        for i in nums:    
            if result == i:
                count += 1
            else:
                count -= 1
            
            if count == -1:
                count = 1
                result = i
                
        return result
        
        
#         d = Counter(nums)
        
#         for k,v in d.items():
#             if v > floor(len(nums)/2):
#                 return k



        
