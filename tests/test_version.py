"""Test the module version."""
from vivintpy import __version__


def test_version() -> None:
    """Test version."""
    assert __version__ == "2023.3.3"
