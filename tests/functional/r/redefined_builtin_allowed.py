"""Tests for redefining builtins."""

def function():
    """Allow some redefines."""
    dir = "path"  # allowed in config
    dict = "bad"  # [redefined-builtin]
    print(dir, dict)
