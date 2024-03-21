# Find the sub-array with maximum sum in a given array.

def find_max_sum_subarray(arr: list):
    if not arr or len(arr) == 1:
        return arr
    max_array = [arr[0]]
    max_array_sum = arr[0]
    _map = {max_array_sum: [arr[0]]}
    for i in range(1, len(arr)):
        current_element = arr[i]
        max_array = [*max_array, arr[i]]
        max_array_sum = max_array_sum + arr[i]
        _map[max_array_sum] = max_array
        if current_element > max_array_sum:
            max_array_sum = current_element
            max_array = [arr[i]]
            _map[max_array_sum] = max_array
    
    max_array = []
    _sum = None
    for key, value in _map.items():
        if _sum is None or key > _sum:
            _sum = key
            max_array = value

    return max_array


print(find_max_sum_subarray([1, -3, 2, 1, -1]))