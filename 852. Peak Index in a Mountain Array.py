class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        biggest = arr[0]
        length = len(arr)
        for i in range(length) :
            if arr[i] > biggest :
                biggest = arr[i]
        return arr.index(biggest)
