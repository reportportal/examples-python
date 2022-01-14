
def test_launch_url_get(rp_logger, rp_launch_id, rp_endpoint, rp_project):
    """
    This is a test which gets Launch ID, Report Portal endpoint and Project
    Name from fixtures in `conftest.py` and prints the result in logs, both: in
    console and on Report Portal
    """
    rp_logger.info("Got launch ID: %s", rp_launch_id)
    rp_logger.info("Launch URL: %s/ui/#%s/launches/all/%s", rp_endpoint,
                   rp_project, rp_launch_id)
    assert True
