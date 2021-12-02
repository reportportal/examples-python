
class Tests:

    def test_in_class(self, rp_logger):
        """
        This is my test inside `Tests` suite
        """
        rp_logger.info("A simple test")
        assert True is True
