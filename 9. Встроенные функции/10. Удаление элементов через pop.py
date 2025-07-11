def pop_until_zero(nums):
    extracted = []
    while nums:
        num = nums.pop()
        if num == 0:
            break
        extracted.append(num)
    return extracted

print(pop_until_zero([5, 3, 1, 0, 7, 8]))