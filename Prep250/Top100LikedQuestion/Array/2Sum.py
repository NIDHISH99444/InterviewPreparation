


def twoSum(nums,target):
    map={}
    for i in range(len(nums)):
        if target-nums[i] not in map:
            map[nums[i]]=i
        else:
            return map[target-nums[i]],i


nums = [3,3]
target = 6

print(twoSum(nums,target))