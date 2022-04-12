#  Copyright (c) 2022 https://reportportal.io .
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License
"""An example test which generates Launch URL."""


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
