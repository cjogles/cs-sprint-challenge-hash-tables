def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # 1. iterate over list 1 and list 2 and save the common numbers in a cache
    # 2. iterate over ALL other lists (3 onwards)
    #    - If cache contains a number that the list 3 (or any other) doesn't have: remove from cache
    #    - We do this because we now know those numbers aren't in every list. 
    # 3. Then return the cache! You have a list of all numbers that are in every list.
    cache = {}
    keys_to_delete = []
    first_list = {}
    for i in arrays[0]:
        first_list[i] = True
    for i in arrays[1]:
        if i in first_list:
            cache[i] = True

    for i in range(2, len(arrays)): 
        for j in cache:
            if j not in arrays[i]:
                keys_to_delete.append(j)
    
    if len(keys_to_delete) > 0:
        for i in keys_to_delete:
            cache.pop(i)
        
    return (list(cache))

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
