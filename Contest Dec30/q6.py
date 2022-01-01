def check_zero(num):
    return bool(num)

nums = list(map(int, input().split()))
print(sorted(nums, reverse=True, key=check_zero))