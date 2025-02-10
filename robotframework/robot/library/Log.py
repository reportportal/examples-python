#  Copyright 2021 EPAM Systems
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import logging

from robotframework_reportportal import logger
from reportportal_client.helpers import guess_content_type_from_bytes


def item_log(level: str, message: str, attachment: dict = None):
    logger.write(message, level, attachment=attachment)


def launch_log(level: str, message: str, attachment: dict = None):
    logger.write(message, level, attachment=attachment, launch_log=True)


def binary_log(level: str, message: str, file_name: str, attachment: bytes):
    logger.write(
        message,
        level,
        attachment={
            "name": file_name,
            "data": attachment,
            "mime": guess_content_type_from_bytes(attachment),
        },
        launch_log=False,
    )


def mute_reportportal_logs():
    listener_logger = logging.getLogger("robotframework_reportportal.listener")
    listener_logger.setLevel(100)
    service_logger = logging.getLogger("robotframework_reportportal.service")
    service_logger.setLevel(100)
    client_logger = logging.getLogger("reportportal_client.service")
    client_logger.setLevel(100)
