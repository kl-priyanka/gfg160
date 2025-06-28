class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        sorted_array=sorted(arr)
        set_=set(sorted_array)
        n = len(set_)
        if n < 2:
            return -1
        set_sort = sorted(set_)
        arr1=[*set_sort]
        return arr1[-2]