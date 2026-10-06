def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError
    nums.sort()
    return nums[0], nums[-1]

print(min_max([3,-1,5,5,0]))
print(min_max([42]))
print(min_max([-5,-2, -9]))
try:
    print(min_max([]))
except ValueError:
    print('ValueError')
print(min_max([1.5, 2, 2.0, -3.1]))


print('')


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    uni_set=set(nums)
    result=list(uni_set)
    n=len(result)
    for i in range (n):
        for j in range(i+1,n):
            if result[i]>result[j]:
                result [i], result[j] = result[j], result [i]
    return result

print(unique_sorted([3,1,2,1,3]))
print(unique_sorted([]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([1.0,1,2.5,2.5,0]))


print('')


def flatten(mat: list[list | tuple]) -> list:
    result=[]
    for i in mat:
        if type(i) == list or type(i) == tuple:
            result.extend(i)
        else: 
            raise TypeError
    return result

print(flatten([[1,2],[3,4]]))
print(flatten([[1,2], (3,4,5)]))
print(flatten([[1], [],[2,3]]))
try:
    print(flatten([[1,2], 'ab']))
except TypeError:
    print('TypeError')


        
