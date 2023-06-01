def find_duplicate(nums):
    if (
        nums is None
        or len(nums) <= 1
        or any(not isinstance(num, int) or num < 0 for num in nums)
    ):
        return False

    nums.sort()

    for index in range(1, len(nums)):
        if nums[index] == nums[index - 1]:
            return nums[index]

    return False
