"""A simple example test in a class with a parameter."""
import pytest


class Tests:

    @pytest.mark.parametrize('param', ['param'])
    def test_in_class_parameterized(self, rp_logger, param):
        """
        This is my test inside `Tests` class with a parameter
        """
        rp_logger.info("A simple test with param: " + param)
        assert True
