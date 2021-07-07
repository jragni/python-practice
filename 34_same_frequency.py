from collections import Counter

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return digit_counter(num1) == digit_counter(num2)

def digit_counter(num):
    digits = str(num)
    digit_counts = {}
    for digit in digits:
        if digit in digit_counts:
            digit_counts[digit] += 1
        else:
            digit_counts[digit] = 1

    return digit_counts

