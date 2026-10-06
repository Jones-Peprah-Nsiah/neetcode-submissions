class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        i will create an empty hashset to keep track of already seen numbers.
        i will  iterate through the array once if num is already in hashset i return true that is it contains duplicate if not i add number to the hashet and continue, if after the iteration no number is already in the hashset i return False. Time is  O(n) as we iterate through the array n number of times. space is O(n) because the hashset stores n numbers.

        """

        seen=set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False

        