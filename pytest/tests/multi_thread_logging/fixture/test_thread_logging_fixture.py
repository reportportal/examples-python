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

This way requires `rp_thread_logging` parameter to be enabled, it does support
Threads with overridden `run` method. But it does not support logging in nested
steps inside tests. All logs in such steps will go into base test section.
"""

import logging
import threading
import time

import pytest


class ThreadLogger(threading.Thread):
    """This class logs stuff to a logger."""
    stop_event: threading.Event = threading.Event()

    def __init__(self, logger: logging.Logger = logging.getLogger(__name__)):
        super().__init__()
        self.logger = logger

    def run(self):
        """This function logs stuff to a logger."""

        while self.stop_event.is_set() is False:
            time.sleep(.5)
            self.logger.info(
                "This is a log from a thread: " + self.logger.name)


def create_threaded_logger(name: str):
    """This function creates a thread that logs stuff."""
    thread = ThreadLogger(logging.getLogger(name))
    thread.start()
    return thread


@pytest.fixture(scope="module")
def thread1():
    """This fixture starts a thread that logs in a thread."""
    return create_threaded_logger("thread1")


@pytest.fixture(scope="module")
def thread2():
    """This fixture starts a thread that logs in a thread."""
    return create_threaded_logger("thread2")


def test_threaded_logging(thread1: ThreadLogger, thread2: ThreadLogger):
    """This test logs from multiple threads."""
    logging.info("This is a log from the main thread")
    time.sleep(1)
    thread1.stop_event.set()
    thread2.stop_event.set()
