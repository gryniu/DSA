class Solution:
    def canPartition(self, nums):
        suma = sum(nums)
        n = len(nums)
        if suma % 2 == 1:
            return False
        target = suma // 2  # musimy znalezc subset, ktory sie sumuje do tego targetu

        return -1
nums = [1,5,11,5]
wynik=Solution()
print(wynik.canPartition(nums))