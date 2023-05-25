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
"""Example test configuration for pytest."""

import logging

import pytest
import reportportal_client
from reportportal_client import RPLogHandler


@pytest.fixture(scope='function')
def rp_thread_logger(request):
    logger = logging.getLogger("test." + request.node.name)
    handler = RPLogHandler(
        level=logging.DEBUG,
        filter_client_logs=True,
        endpoint=request.config._reporter_config.rp_endpoint,
        ignored_record_names=('reportportal_client',
                              'pytest_reportportal'),
        rp_client=reportportal_client.current())
    logger.addHandler(handler)
    return logger
