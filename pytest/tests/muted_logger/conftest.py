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
"""Example test configuration for pytest with no RP logs."""

import logging

import pytest
import reportportal_client
from reportportal_client import RPLogger, RPLogHandler


@pytest.fixture(scope='session', autouse=True)
def rp_mute_logger():
    listener_logger = logging.getLogger("robotframework_reportportal.listener")
    listener_logger.setLevel(100)
    service_logger = logging.getLogger("robotframework_reportportal.service")
    service_logger.setLevel(100)
    client_logger = logging.getLogger("reportportal_client.service")
    client_logger.setLevel(100)
