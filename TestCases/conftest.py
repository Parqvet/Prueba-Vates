import pytest
from Base.ConstruirDrive import Base

@pytest.fixture()
def setup():
    base = Base()
    driver = base.get_driver()
    return driver