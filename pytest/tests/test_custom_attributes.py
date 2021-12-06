import pytest


@pytest.mark.scope("smoke")
@pytest.mark.scope("regression")
@pytest.mark.ignored_attribute("test")
def test_custom_attributes_report(rp_logger):
    """
    This is a test with multiple custom markers which shall appear on
    ReportPortal on test's item as different attributes
    """
    rp_logger.info("A test with multiple custom attributes")
    assert True is True
