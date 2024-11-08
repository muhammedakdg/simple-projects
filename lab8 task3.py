def approximate_pi(m: int) -> float:
    """
    Approximates the value of pi using the Leibniz formula up to m terms.

    The formula approximates pi as:
        π ≈ 4 * Σ((-1)^n / (2n + 1)) for n in range 0 to m

    Parameters:
        m (int): The number of terms to include in the approximation.

    Returns:
        float: The approximation of pi rounded to four decimal places.

    Examples:
    >>> approximate_pi(2)
    3.4667
    >>> approximate_pi(4)
    2.8952
    >>> approximate_pi(6)
    3.2837
    >>> approximate_pi(10)
    3.2323
    """
    result = sum((-1)**n / (2 * n + 1) for n in range(m + 1))
    return round(4 * result, 4)