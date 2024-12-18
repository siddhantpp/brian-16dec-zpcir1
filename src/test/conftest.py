# pytest ^7.0.0
import pytest
from ..hello_world.hello_world import main

@pytest.fixture
def hello_world_fixture() -> str:
    """Pytest fixture that provides the expected hello world output.
    
    Returns:
        str: Returns 'Hello, World!' string from the main function
    """
    return main()