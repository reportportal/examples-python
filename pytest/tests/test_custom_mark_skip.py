import pytest


def test_pass_to_show_in_report(rp_logger):
    rp_logger.info("Just a passed test")
    assert True is True


@pytest.mark.command_skip
def test_custom_mark_skip_command_line():
    assert True is False


@pytest.mark.fixture_skip
def test_custom_mark_skip_fixture():
    assert True is False
