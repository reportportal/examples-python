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
from robotframework_reportportal import service


def launch_log(level: str, message: str, attachment: dict = None):
    rq = {
        "time": service.timestamp(),
        "message": message,
        "level": service.RobotService.log_level_mapping[level],
        "attachment": attachment,
    }
    service.RobotService.rp.log(**rq)
