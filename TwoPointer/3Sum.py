class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()

        for i in range(len(nums) - 2):
            left_pointer = i + 1
            right_pointer = len(nums) - 1

            while left_pointer < right_pointer:
                if nums[i] + nums[left_pointer] + nums[right_pointer] == 0:
                    answer.add((nums[i], nums[left_pointer], nums[right_pointer]))
                    left_pointer += 1
                    right_pointer -= 1
                elif nums[i] + nums[left_pointer] + nums[right_pointer] < 0:
                    left_pointer += 1
                else:
                    right_pointer -= 1

        return answer