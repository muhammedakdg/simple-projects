def remove_vowels(s: str) -> str:
    """
    Removes all vowels ('a', 'e', 'i', 'o', 'u', both uppercase and lowercase) from the given string.

    Parameters:
        s (str): The input string from which vowels will be removed.

    Returns:
        str: The string with all vowels removed.

    Raises:
        AssertionError: If the input contains characters other than letters and spaces.

    Examples:
    >>> remove_vowels("Python Programming")
    'Pythn Prgrmmng'
    >>> remove_vowels("abc")
    'bc'
    >>> remove_vowels("a")
    ''
    >>> remove_vowels("AEIOU")
    ''
    >>> remove_vowels("hello world")
    'hll wrld'
    """
    assert isinstance(s, str) and all(c.isalpha() or c.isspace() for c in s), "Input must be a string containing only letters and spaces."

    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)