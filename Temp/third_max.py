def thirdMax (nums):
    first=second=third = float('-inf')
    for num in nums:
        if num > first:
            temp = first
            temp2 = second
            first = num
            second = temp
            third = temp2
        elif num > second and num < first:
            temp = second
            second = num
            third = temp
        elif num > third and num < second:
            third = num
    return third