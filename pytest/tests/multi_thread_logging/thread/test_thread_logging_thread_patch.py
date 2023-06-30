#  Copyright (c) 2023 https://reportportal.io .
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
"""An example which shows a way to log from Python threads.

This way requires `rp_thread_logging` parameter to be enabled and it does not
support Threads with overridden `run` method. But it does support logging in
nested steps inside tests.
"""

import logging
import threading

from reportportal_client.steps import step

log = logging.getLogger(__name__)


def worker():
    log.info("TEST_INFO")
    log.debug("TEST_DEBUG")


def test_log():
    t = threading.Thread(target=worker)
    log.info("TEST_BEFORE_THREADING")
    with step("Some nesting where the thread logs should go"):
        t.start()
    t.join()
