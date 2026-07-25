def generate_code(prefix: str, number: int, length: int = 6):
    """
    Generate business code.

    Example:
    CUS000001
    PRD000123
    """

    return f"{prefix}{number:0{length}}"