# MEDIAN and INTERQUARTILE RANGE
nums = input('Enter list of numbers: ')
nums = nums.split()
num = []
for i in nums:
    i = int(i)
    num.append(i)
num = num.sort()
if len(num) % 2 == 1:
    median = num[(len(num)+1)//2 - 1]
    if (len(num)-1) % 4 == 0:
        Q1 = num[(len(num)-1)//4]
        Q3 = num[(len(num)-1)//4*3]
    else:
        Q1 = (num[(len(num)-1)//4] + num[(len(num)-1)//4 + 1])/2
        Q3 = (num[(len(num)-1)//4+len(num)//2]+num[(len(num)-1)//4+1 +len(num)//2])/2
    IQR = Q3 - Q1
    print(f'Median is {median}')
    print(f'IQR is {IQR}')
else:
    median = (num[len(num)//2 - 1] + num[len(num)//2])/2
    if len(num) % 4 == 0:
        Q1 = (num[len(num)//4-1] + num[len(num)//4])/2
        Q3 = (num[len(num)//4-1 + len(num)//2] + num[len(num)//4 + len(num)//2])/2
    else:
        Q1 = num[len(num)//4]
        Q3 = num[len(num)//4 + len(num)//2]
    IQR = Q3 - Q1
    print(f'Median is {median}')
    print(f'IQR is {IQR}')
