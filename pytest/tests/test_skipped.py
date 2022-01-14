import pytest


def test_pass_to_show_in_report(rp_logger):
    rp_logger.info("Just a passed test")
    assert True


@pytest.mark.skip(reason='no way of currently testing this')
def test_the_unknown():
    assert False


@pytest.mark.command_skip
def test_custom_mark_skip_command_line():
    assert False


@pytest.mark.fixture_skip
def test_custom_mark_skip_fixture():
    assert False


def test_inner_skip_test():
    pytest.skip("Skip from test insides")
