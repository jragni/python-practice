def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    
    flipped = ""
    for char in phrase:
        if char.lower() == to_swap or char.upper() == to_swap:
            flipped += char.swapcase()
        else:
            flipped += char
    return flipped