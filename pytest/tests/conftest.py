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
from reportportal_client import RPLogger, RPLogHandler


# Uncomment the following lines to get full HTTP logging in console
# from http.client import HTTPConnection
# HTTPConnection.debuglevel = 1


@pytest.fixture(scope='session')
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.setLoggerClass(RPLogger)
    return logger


@pytest.fixture(autouse=True)
def skip_by_mark(request):
    if request.node.get_closest_marker('fixture_skip'):
        pytest.skip('skip by fixture')


@pytest.fixture(scope='session')
def rp_launch_id(request):
    if hasattr(request.config, "py_test_service"):
        return request.config.py_test_service.rp.launch_id


@pytest.fixture(scope='session')
def rp_endpoint(request):
    if hasattr(request.config, "py_test_service"):
        return request.config.py_test_service.rp.endpoint


@pytest.fixture(scope='session')
def rp_project(request):
    if hasattr(request.config, "py_test_service"):
        return request.config.py_test_service.rp.project
