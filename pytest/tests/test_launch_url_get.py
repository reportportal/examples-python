
def test_launch_url_get(rp_logger, rp_launch_id, rp_endpoint, rp_project):
    rp_logger.info("Got launch ID: %s", rp_launch_id)
    rp_logger.info("Launch URL: %s/ui/#%s/launches/all/%s", rp_endpoint,
                   rp_project, rp_launch_id)
    assert True is True
