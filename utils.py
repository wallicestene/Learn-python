def get_max_num(nums):
    max_num = 0
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num
