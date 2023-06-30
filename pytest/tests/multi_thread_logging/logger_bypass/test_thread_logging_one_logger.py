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
#
#  https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License
"""An example which shows a way to log from Python threads.

This way does not require `rp_thread_logging` parameter to be enabled.
'rp_thread_logger' argument is initialized inside `conftest.py` script in the
same module.
"""

import logging
import threading

logger = logging.getLogger(__name__)


def working_method(thread_logger):
    thread_logger.info("I'm logging in a thread")


def test_thread_logging(rp_thread_logger):
    t = threading.Thread(target=lambda: working_method(rp_thread_logger))
    logger.info("TEST_BEFORE_THREADING")
    t.start()
    t.join()
