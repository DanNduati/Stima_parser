import pytest
from Stimaparser.parser import Stimaparser


# define a parser fixture
@pytest.fixture(scope="module")
def test_matches():
    parser = Stimaparser()
    yield parser
