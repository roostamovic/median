# MEDIAN and INTERQUARTILE RANGE
def calculate_median_iqr(nums):
    nums = sorted(list(nums))
    if len(nums) % 2 == 1:
        median = nums[(len(nums)+1)//2 - 1]
        if (len(nums)-1) % 4 == 0:
            Q1 = nums[(len(nums)-1)//4]
            Q3 = nums[(len(nums)-1)//4*3]
        else:
            Q1 = (nums[(len(nums)-1)//4] + nums[(len(nums)-1)//4 + 1])/2
            Q3 = (nums[(len(nums)-1)//4+len(nums)//2]+nums[(len(nums)-1)//4+1 +len(nums)//2])/2
        IQR = Q3 - Q1
        
    else:
        median = (nums[len(nums)//2 - 1] + nums[len(nums)//2])/2
        if len(nums) % 4 == 0:
            Q1 = (nums[len(nums)//4-1] + nums[len(nums)//4])/2
            Q3 = (nums[len(nums)//4-1 + len(nums)//2] + nums[len(nums)//4 + len(nums)//2])/2
        else:
            Q1 = nums[len(nums)//4]
            Q3 = nums[len(nums)//4 + len(nums)//2]
        IQR = Q3 - Q1
        
    print(f'Median of {nums} is {median}')
    print(f'IQR of {nums} is {IQR}')
