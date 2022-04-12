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
"""An example test which shows different types of nested steps."""
from reportportal_client import step


@step("test", rp_client=None)
def nested_step():
    print("Inside nested step")


@step
def two_level_nested_step():
    nested_step()
    print("Inside nested step")


@step
def nested_step_params(param1, param2, named_param=None):
    print("Inside nested step with params")


@step("Custom name nested step")
def custom_name():
    print("Inside nested step with custom name")


def test_function_level_nested_steps_start_stop():
    nested_step()
    nested_step_params(1, 2, named_param="test")
    two_level_nested_step()
    custom_name()

    with step("Code level nested step", {"test": "value"}):
        print("Inside code-level nested step")
