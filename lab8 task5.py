def reverse_str(s: str) -> str:
    """
    Reverses the given string.

    Parameters:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Examples:
    >>> reverse_str("abcde")
    'edcba'
    >>> reverse_str("a")
    'a'
    >>> reverse_str("123")
    '321'
    >>> reverse_str("")
    ''
    >>> reverse_str("hgfedcba")
    'abcdefgh'
    >>> reverse_str("!@# $%^")
    '^%$ #@!'
    """
    assert isinstance(s, str), "Input must be a string"
    return s[::-1]