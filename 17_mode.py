def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    highest_frequency_num = 0
    highest_frequency = 0

    for num in nums:
        if nums.count(num) > highest_frequency:
            highest_frequency = nums.count(num)
            highest_frequency_num = num
    return highest_frequency_num
    
