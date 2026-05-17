import pytest
def test_thirdprogram():
    msg="hello"
    assert msg == "hi","test failed"

@pytest.mark.xfail
def test_fourthprogram():
    a=4
    b=5
    assert a+1 == 5,"addition do not match"

@pytest.fixture()
def setup():
    print("ececute 1st")

def test_foirthprogram(setup):
    print("ececute 2nd")