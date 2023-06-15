class ConfigurationError(Exception):
    """Raised while reading configuration files."""

    pass


class ElementNotFoundError(Exception):
    """Raised when the desired element is not present in the DOM"""

    pass
