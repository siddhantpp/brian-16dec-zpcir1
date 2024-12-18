# pytest version 7.0.0
from ..hello_world.hello_world import main

def test_hello_world():
    """Test that verifies the hello world function returns the correct string."""
    result = main()
    assert result == 'Hello, World!'