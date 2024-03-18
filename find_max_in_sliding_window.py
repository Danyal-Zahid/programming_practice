def find_max(nums: list[int]):
    result = None
    for i in nums:
        if result is None or i > result:
            result = i
    return result

def find_max_sliding_window(nums: list[int], w: int):
    i = 0
    j = 0
    running_max = None
    output = []
    while True:
        if i == 0:
            while j - i < w:
                if running_max is None or nums[j] > running_max:
                    running_max = nums[j]
                j += 1
            output.append(running_max)
            i += 1
        else:
            if j >= len(nums):
                break
            element_removed_from_window = nums[i - 1]
            new_element = nums[j]
            if element_removed_from_window < running_max:
                if running_max < new_element:
                    running_max = new_element
            elif element_removed_from_window == running_max:
                if new_element >= running_max:
                    running_max = new_element
                else:
                    running_max = find_max(nums[i:j+1])
            output.append(running_max)
            i += 1
            j += 1
    return output

print(find_max_sliding_window([10,6,9,-3,23,-1,34,56,67,-1,-4,-8,-2,9,10,34,67] , 3))