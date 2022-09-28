import pytest
from first_project import find_if_not_prime_number


@pytest.fixture
def example_fixture():
    return 10


def test_find_if_not_prime_number_with_non_prime(example_fixture):
    assert find_if_not_prime_number(example_fixture) is True


def test_find_if_not_prime_number_with_prime():
    assert find_if_not_prime_number(5) is False
