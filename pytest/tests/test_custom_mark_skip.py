import pytest


@pytest.mark.custom
def test_custom_mark_skip():
    assert True is True
