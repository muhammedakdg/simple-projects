def encrypt(message: str, shift: int) -> str:
    """
    Encrypts a message using a Caesar cipher with a specified shift.

    For each letter in the message, shifts the letter by the specified number
    of positions in the alphabet. Non-uppercase letters are not modified.

    Parameters:
        message (str): The message to encrypt.
        shift (int): The number of positions to shift each letter.

    Returns:
        str: The encrypted message.

    Examples:
    >>> encrypt("ATTACK AT DAWN", 3)
    'DWWDFN DW GDZQ'
    >>> encrypt("HELLO", 4)
    'LIPPS'
    >>> encrypt("PYTHON", 5)
    'UDYMTS'
    >>> encrypt("GOOD MORNING", 10)
    'QYYX WBYXSCQX'
    """
    encrypted_message = ""
    for char in message:
        if 'A' <= char <= 'Z':  # Check if the character is an uppercase letter
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_message += new_char
        else:
            encrypted_message += char  # Non-uppercase letters remain unchanged
    return encrypted_message