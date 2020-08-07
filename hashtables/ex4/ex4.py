def has_negatives(the_input):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for i in the_input:
        if i > 0:
            cache[i] = 0
        else:
            continue
    for i in the_input:
        if i < 0:
            i = -i 
            if i in cache:
                result.append(i)
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
