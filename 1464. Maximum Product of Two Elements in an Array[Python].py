class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        biggest = 0
        second_biggest = 0
        for i in nums: 
            if i > biggest : 
                second_biggest = biggest
                biggest = i
            else : 
                second_biggest = max(second_biggest,i)

        return (biggest-1)*(second_biggest-1)



