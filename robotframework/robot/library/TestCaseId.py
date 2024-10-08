#  Copyright 2024 EPAM Systems
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from typing import Optional

from robot.libraries.BuiltIn import BuiltIn


def case_id(test_case_id_pattern: Optional[str]) -> None:
    built_in = BuiltIn()
    if not test_case_id_pattern:
        return
    suite_metadata = str(built_in.get_variable_value('${rplaunchattributes}')).split()
    env = None
    for value in suite_metadata:
        if value.strip().lower().startswith('env:'):
            env = value.strip().split(':', maxsplit=1)[1]
            break
    if not env:
        return
    built_in.set_tags('test_case_id:' + test_case_id_pattern.format(env_var=env))
