import sys

import pytest


@pytest.mark.skipif(sys.version_info < (3, 0),
                    reason="requires python3 or higher")
def test_skip_python_2_7(rp_logger):
    rp_logger.info("The test should not run on python 2.7")
    assert True is True


@pytest.mark.skipif(sys.version_info > (2, 7),
                    reason="requires python3 or higher")
def test_skip_python_3_and_higher(rp_logger):
    rp_logger.info("The test should not run on python3 and higher")
    assert True is True
