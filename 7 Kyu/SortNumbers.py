# Given an array, sort the numbers
# Make it so that it can handle null/nil value


def solution(nums):
    if nums is None or len(nums) <= 0:
        return []
    return sorted(nums)