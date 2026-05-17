import pytest

import pytest
@pytest.mark.smoke
def test_firstprogram():
    print("hello")

@pytest.mark.skip
def test_secondprogram():
    print("hello morning")

def test_fourthprogram():
    print("hello morning")

