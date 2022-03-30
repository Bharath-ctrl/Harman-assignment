import pytest
@pytest.fixture(    scope="session" , autouse=True  )
def setUp():
    print("Open Amazon app")
    print("User login")
    yield
    print("Logout")
    print("Close Amazon App")
