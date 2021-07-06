def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase = phrase.lower()
    if " " in phrase:
        phrase = phrase.replace(" ", "")

    left = 0
    right = len(phrase) - 1
    while(left < right ):
        if phrase[left] != phrase[right]:
            return False
        left+=1
        right-=1
    return True